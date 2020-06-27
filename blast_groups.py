import hou, random

nodes = hou.selectedNodes()

if nodes:
    for node in nodes:
        if node.type().category() == hou.sopNodeTypeCategory():
            geo = node.geometry()
            primGroups = geo.primGroups()
            ptGroups = geo.pointGroups()
            if (len(ptGroups) != 0):
                groups = primGroups + ptGroups
            if groups:
                count = 1
                for grp in groups:
                    count += 3
                    blast = node.createOutputNode('blast', 'blastgrp')
                    blast.parm('group').set(grp.name())
                    blast.parm('negate').set(1)
                    blast.setPosition(node.position())
                    blast.move([count, -1])
                    
                    randCd = hou.Color((random.random(),random.random(),random.random()))
                    
                    blast.setColor(randCd)
                    
                    mtl = blast.createOutputNode('material')
                    mtl.setColor(randCd)
                    
                    null = mtl.createOutputNode('null', 'OUT_BLASTGROUP_1')
                    null.setColor(hou.Color((0.1,0.5,0.0)))
                    
                    path = node.path()
                    geo = hou.node('/obj').createNode('geo',blast.name() + '_render', run_init_scripts=0) 
                    geo.move([0, -count/4])
                    geo.setColor(hou.Color((0.0,0.6,1.0)))
                    geo.setDisplayFlag(0)
                    
                    objMerge = geo.createNode('object_merge')
                    objMerge.parm('objpath1').set(path)
                    objMerge.setColor(hou.Color((1.0,0.8,0.0)))
                    objMerge.parm('xformtype').set(1)
                    nullRender = objMerge.createOutputNode('null', 'OUT_RENDER')
                    nullRender.setColor(hou.Color((0.1,0.5,0.0)))
                    nullRender.setRenderFlag(1)