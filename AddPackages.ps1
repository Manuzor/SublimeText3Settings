<#
  .SYNOPSIS
    Adds some default packages to the "User/Package Control.sublime-settings" file.
#>
$ExtraPackages = @(
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
  "Theme - SoDaReloaded";
  "VimL";
)

$PSScriptRoot
$TargetFilePath = Join-Path -Resolve $PSScriptRoot "../User/Package Control.sublime-settings"

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
