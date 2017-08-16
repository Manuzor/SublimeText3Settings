<#
  .SYNOPSIS
    Adds some default packages to the "User/Package Control.sublime-settings" file.
#>
$ExtraPackages = @(
  "Theme - SoDaReloaded";
  "Alignment";
  "AutoHotkey";
  "CMakeEditor";
  "EditorConfig";
  "FASTBuild";
  "FileDiffs";
  "Git";
  "GitGutter";
  "HexViewer";
  "IDL-Syntax";
  "Indent XML";
  "Markdown Preview";
  "Package Control";
  "PowerShell";
  "RevertFontSize";
  "Schemr";
  "SDLang";
  "Shader Syntax (GLSL HLSL Cg)";
  "SideBarEnhancements";
  "Solarized Color Scheme";
  "VimL";
)

$TargetFilePath = Join-Path $PSScriptRoot "../User/Package Control.sublime-settings"

if($False)
# if(Test-Path $TargetFilePath)
{
  $Content = Get-Content -Raw $TargetFilePath
  $Json = ConvertFrom-Json $Content

  foreach($Package in $ExtraPackages)
  {
    if(!($Json.installed_packages -contains $Package))
    {
      $Json.installed_packages += $Package
    }
  }

  $NewContent = ConvertTo-Json $Json
  Set-Content -Path $TargetFilePath -Value $NewContent
}
else
{
  $NewContent = @"
{
`t"installed_packages":
`t[
`t`t"$($ExtraPackages -join "`",`n`t`t`"")"
`t]
}
"@

  New-Item -Force (Split-Path -Parent $TargetFilePath) -ItemType Directory
  Set-Content -Path $TargetFilePath -Value $NewContent
}
