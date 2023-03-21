# AeroWitter-Developer-Option-Finder
![image](https://user-images.githubusercontent.com/20567089/226596954-b4aebf30-f020-4734-826c-3b3cc91ac93e.png)
<br>
<br>
<h1>How to use:</h1>
<b>Select AeroWitter decompiled folder</b> (button):
<br>To select the folder path of the decompiled Twitter APK file.
<br><br>e.g.:

 `D:/MyFiles/DecompiledAPKS/Twitter`
<br><br><b>Select json save path</b> (button):
<br>To select which folder and which file the output values will be saved to.
<br><br>e.g.:

 `D:/MyFiles/DecompiledAPKS/output.json`

> Make sure the file name ends with .json suffix. 

<br><br><b>Search caller code</b> (text box):
<br>You can select the version number you want to process from the list or you can type caller code yourself.
<br>The version number and correct calling code are being synchronized from file [AeroWitter-boolean.json](https://github.com/hazarbozkurt/AeroWitter-Developer-Option-Finder/blob/main/AeroWitter-boolean.json). Whenever we manage to find some spare time, we'll make sure to update this file. 

If you want to type caller code yourself:
The text box must have the correct caller to find the correct `const-string` value.
This calling code snippet changes with every version of Twitter due to Twitter’s encryption. Therefore, you need to manually find a `const-string` key of developer option type and use calling codes like `Lvlu;->b(Ljava/lang/String;Z)Z` under the key you found to find all other developer option keys.

For example, in version <b>9.75.0-release.0 (29750000)</b> this code is `Lr9v;->b(Ljava/lang/String;Z)Z`, while in version <b>9.80.0-release.0 (29800000)</b> it is `Lvlu;->b(Ljava/lang/String;Z)Z`.

A screenshot of the key code:
<br>![AeroWitter](https://user-images.githubusercontent.com/20567089/226435655-28d41f0f-71f6-458a-b247-12636c1d21dd.png)

<br><br>**How to find version number of decompiled Twitter APK:**
<br>To find the version number of the Twitter APK file you decompiled, check out the following file:
`D:/MyFiles/DecompiledAPKS/Twitter/apktool.yml`

![image](https://user-images.githubusercontent.com/20567089/226440152-2d12a0d5-dc88-4311-9773-09dd2eefd10f.png)

<br>
<br>

# How to use output Json file?
The JSON file is being created to be compatible with Canned Replies. You can download the Canned Replies app from the Google Play Store by clicking [here](https://play.google.com/store/apps/details?id=com.tinaciousdesign.cannedreplies). You can import your JSON file using the ‘Import’ option in Canned Replies. With Canned Replies, you can copy each value with a single click.
