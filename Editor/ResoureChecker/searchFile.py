import os
import re
import sys


def fileNameFilter(pattern, fn):
	return re.match(pattern, fn)

def searchInFiles(pattern, paths):
	foundFiles = []
	for path in paths :
		with open(path, 'r') as file:
			content = file.read()
			if re.findall(pattern, content) :
				foundFiles.append(path)
	return foundFiles

def findFiles(filter, pattern, workingDir) :
	foundFiles = []
	for root, dirs, files in os.walk(workingDir):
		for fn in files:
			path = os.path.join(root, fn)
			if filter(pattern, fn) or filter(pattern, path):
				foundFiles.append(path)
			pass
	return foundFiles

def getGUID(path):
	guid = ""
	with open(path, 'r') as f :
		lines = f.readlines()
		guid = lines[1][6:-1]
	return guid	

def getEnvArg(name):
	count = 0
	argvLen = len(sys.argv)
	while count < argvLen :
		s = sys.argv[count]
		if s == name and count + 1 < argvLen :
			return sys.argv[count + 1]
		count += 1

def findDependenciesWithManyLevels(searchName, dependList, workingDir):
	metaExt = ".meta"
	count = 0
	ret = {}
	while(count < len(dependList)-1):
		childNames = []
		if(count == 0):
			childNames.append(searchName)
		else:
			childNames += ret[dependList[count]]

		parentId = count + 1
		paths = []
		foundParent  = []
		for childName  in childNames :
			metaChildPattern = r'^' + childName + metaExt
			parentPattern = r'.*' + dependList[parentId] + r'$'
			childFiles = findFiles(fileNameFilter, metaChildPattern, workingDir)
			if len(childFiles) > 0 :
				path = childFiles[0]
				guid = getGUID(path)
				paths += findFiles(fileNameFilter, parentPattern, workingDir)
				foundParent += searchInFiles(guid, paths)
		pass
		count += 1

		ret[dependList[parentId]] = foundParent
	return ret

def main() :
	fileName = "299_Texture.jpg"
	matExt = ".mat"
	prefabExt = ".prefab"
	workingDir = "/Volumes/Data/Projects/Unity/9fury/rot_client/ROT/Assets/Resources"
	fName = getEnvArg("-name")
	if fName:
		fileName = fName

	folder = getEnvArg("-path")
	if folder:
		workingDir = folder

	assetsType = getEnvArg("-type")
	dependList = ["none"]
	if(assetsType == "texture") :
		dependList += [matExt, prefabExt]
	else :
		dependList += [prefabExt]
	ret = findDependenciesWithManyLevels(fileName, dependList, workingDir)
	ret_string = str(ret).replace("\'","\"")
	print ret_string
	

if __name__ == "__main__":
	main()
