using UnityEngine;
using System.Collections;
using UnityEditor;
using System.Diagnostics;

public class ResourceChecker {

	static string GetAssetName(Object obj)
	{
		string assetPath = AssetDatabase.GetAssetPath(obj);
		string[] assetNames = assetPath.Split(new char[]{'/'});
		string assetName = assetNames[assetNames.Length-1];
		return assetName;
	}

	[MenuItem("Assets/FindPrefabsByMaterial")]
	static void FindByMaterial()
	{
		Find(GetAssetName(Selection.activeObject), "material");
	}

	[MenuItem("Assets/FindMaterialsAndPrefabsByTexture")]
	static void FindByTexture()
	{
		Find(GetAssetName(Selection.activeObject), "texture");
	}

	static void Find(string assetName, string type)
	{
		string workingDir = Application.dataPath + "/Resources/";
		Process p = new Process();
		p.StartInfo.WorkingDirectory = Application.dataPath + "/Editor/ResoureChecker/";
		p.StartInfo.UseShellExecute = false;
		p.StartInfo.FileName = "python";
		p.StartInfo.Arguments = "searchFile.py -type "+ type + " -path " + workingDir  + " -name " + assetName;    
		p.StartInfo.RedirectStandardError=true;
		p.StartInfo.RedirectStandardOutput=true;
		p.StartInfo.CreateNoWindow = true;
		p.Start();
		string output = p.StandardOutput.ReadToEnd();
		UnityEngine.Debug.Log(output);
		p.WaitForExit();
		p.Close();
	}
}