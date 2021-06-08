Install-WindowsFeature -name Web-Server -IncludeManagementTools

remove-item 'C:\\inetpub\\wwwroot\\iisstart.htm'

$html = @"
<html>
<head>
<title>Hello World</title>
<style>
.center-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
}
</style>
</head>
<body>
   <div class="center-screen">
        <h4>Hello World from $env:computername</h4>
   </div>
</body>
</html>
"@

Add-Content -Path 'C:\\inetpub\\wwwroot\\iisstart.htm' -Value ('Hello World from ' + $html)