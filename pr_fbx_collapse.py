import hou, os
sel = hou.selectedNodes()
if sel:
    for s in sel:
        out = s.parent().createNode('geo', run_init_scripts=0)
        out.moveToGoodPosition()
        new_shop =  out.createNode('shopnet', 'SHADERS')
    
        geo = [x for x in s.children() if x.type().name() == 'geo']
        old_shop = hou.node(s.path() + '/materials')
        hou.copyNodesTo(old_shop.children(), new_shop)


        m = out.createNode('merge')   
        delete = []
        delete.append(m)
        
        material_dict = {}
        for g in geo:
            material = g.parm('shop_materialpath').eval()
            if material != '':
                material = material.split('/')[-1]
                material_dict [g.name()] = material
            else:
                mat_nodes = [x for x in g.children() if x.type().name() == 'material']
                for i in mat_nodes:
                    num_materials = i.parm('num_materials').eval()
                    num = 0
                    while num < num_materials:
                        num+=1
                        material = i.parm('shop_materialpath' + str(num)).eval().split('/')[-1]
                        mat_group = i.parm('group' + str(num)).eval()
                        material_dict [mat_group] = material
            om = out.createNode('object_merge')
            om.parm('objpath1').set(g.path())
            om.parm('xformtype').set(1)
        
            gr = om.createOutputNode('group')
            gr.parm('crname').set(g.name())
        
            m.setNextInput(gr)
            delete += [om, gr]
    
        m.moveToGoodPosition()
        
        rop = m.createOutputNode('rop_geometry')
        delete.append(rop)
        path = geo[0].children()[0].parm('file').eval().split('#')[0]   
        geoFile = os.path.splitext(path)[0] + '.bgeo'
        
        rop.parm('sopoutput').set(geoFile)
        rop.render()
        
        file = out.createNode('file')
        file.parm('file').set(geoFile)
        file.setColor(hou.Color((1.0,0.8,0.0)))

        new_shop.setColor(hou.Color((1.0,0.0,0.0)))
        new_shop.setPosition(file.position())
        new_shop.move([-1,0])
        
        map(lambda x: x.destroy(), delete)
        s.setDisplayFlag(0)

        mat = file.createOutputNode('material')
        tabs = mat.parm('num_materials')

        mat.setDisplayFlag(1)
        mat.setRenderFlag(1)
        
        mat_count = len(material_dict.keys())
        tabs.set(mat_count)
        num = 0
        while num < mat_count:
            group = mat.parm('group' + str(num+1))
            group.set(material_dict.keys()[num])
            material = mat.parm('shop_materialpath' + str(num+1))
            mat_path = new_shop.path() + '/' + material_dict.values()[num]
            material.set(mat_path)
            num += 1
            
            
        
        
        
        