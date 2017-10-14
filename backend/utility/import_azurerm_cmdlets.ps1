$cmdlets = Get-Command -Module AzureRM | Select-Object -Property @{Name='name'; Expression={$PSItem.Name}}, @{Name='verb'; Expression={$PSItem.Verb}}, @{Name='noun'; Expression={$PSItem.Noun}}, @{Name='module'; Expression={$PSItem.ModuleName}} | Sort-Object -Property Noun

foreach ($cmdlet in $cmdlets) {
    $body = ConvertTo-Json $cmdlet
    Invoke-RestMethod -Uri 'http://localhost:8000/api/cmdlet' -Method 'post' -Body $body -ContentType "application/json"
}