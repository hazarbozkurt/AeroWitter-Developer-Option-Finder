# AeroWitter-Developer-Option-Finder
![image](https://user-images.githubusercontent.com/20567089/226429348-fbf93b47-ab19-4c3d-a42a-f218ae4f3a60.png)
<br>
<br>
<h1>How to use:</h1>
<b>Select AeroWitter decompiled folder</b> (button):
<br>To select the folder path of the decompiled Twitter APK file.
<br><br>e.g.:

 `D:/MyFiles/DecompiledAPKS/Twitter`
<br><br><b>Select json save path</b> (button):
<br>To select in which folder and which file the output values will be saved.
<br><br>e.g.:

 `D:/MyFiles/DecompiledAPKS/output.json`

> Make sure the file name ends with .json suffix. 

<br><br><b>Search text</b> (text box):
<br>You can select the version number you want to process from the list or you can type it yourself.

The text box must have the correct caller to find the correct `const-string` value.
This calling code snippet changes with every version of Twitter due to Twitter’s encryption. Therefore, you need to manually find a `const-string` key of developer option type and use calling codes like `Lvlu;->b(Ljava/lang/String;Z)Z` under the key you found to find all other developer option keys.

For example, in version <b>9.75.0-release.0 (29750000)</b> this code is `Lr9v;->b(Ljava/lang/String;Z)Z`, while in version <b>9.80.0-release.0 (29800000)</b> it is `Lvlu;->b(Ljava/lang/String;Z)Z`.

A screenshot of the key code:
<br>![AeroWitter](https://user-images.githubusercontent.com/20567089/226435655-28d41f0f-71f6-458a-b247-12636c1d21dd.png)

<br><br>**How to find version number of decompiled Twitter APK:**
<br>The version number and correct calling code are being synchronized from file [AeroWitter-boolean.json](https://github.com/hazarbozkurt/AeroWitter-Developer-Option-Finder/blob/main/AeroWitter-boolean.json). We will update this file as we find time. To find the version number of the Twitter APK file you decompiled, check out the following file:
`D:/MyFiles/DecompiledAPKS/Twitter/apktool.yml`

![image](https://user-images.githubusercontent.com/20567089/226440152-2d12a0d5-dc88-4311-9773-09dd2eefd10f.png)

