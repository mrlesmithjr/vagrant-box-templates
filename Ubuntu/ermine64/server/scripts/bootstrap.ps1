# Bootstrap script for Windows
$ansible_script = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"

# Enable Remote Desktop
(Get-WmiObject Win32_TerminalServiceSetting -Namespace root\cimv2\TerminalServices).SetAllowTsConnections(1, 1)
(Get-WmiObject -Class "Win32_TSGeneralSetting" -Namespace root\cimv2\TerminalServices -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)

# Setup WinRM for Ansible Management
Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression (
  (New-Object System.Net.WebClient).DownloadString($ansible_script))

# Disable Windows firewall
Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled False
