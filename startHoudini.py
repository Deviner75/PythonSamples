import os, subprocess, platform

root = os.path.dirname(__file__)

platform = platform.system()


if 'Windows' in platform:
	app_dir = r"C:\Program Files\Side Effects Software\Houdini 16.0.621\bin\houdinifx.exe"
elif 'Linux' in platform:	
	app_dir = r"some path"
elif 'Mac OS X' in platform:
	app_dir = r"some path"


if not os.path.isfile(app_dir):
	print ("not such file or directory")
	input("Press Enter to exit...")


os.environ['home'] = root
os.environ['HOUDINI_OTLSCAN_PATH'] = os.pathsep.join([os.path.join(root,'lib'),'&'])
os.environ['HOUDINI_PATH'] = os.pathsep.join([os.path.join(root,'houdini_path'),'&'])
os.environ['HOUDINI_SPLASH_FILE'] = os.pathsep.join([os.path.join(root,'splash_screen.jpg')])
subprocess.Popen(app_dir)