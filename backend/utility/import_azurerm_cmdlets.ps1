$cmdlets = Get-Command -Module AzureRM | Sort-Object -Property Noun

foreach ($cmdlet in $cmdlets) {
    $body = @{
        'name' = $cmdlet.Name;
        'verb' = $cmdlet.Name.Split('-')[0];
        'noun' = $cmdlet.Name.Split('-')[1];
        'component' = $cmdlet.Name.Split('-')[1].Replace('AzureRm', '').Replace('Azure', '');
        'module' = $cmdlet.ModuleName
    }
    $body = ConvertTo-Json $body
    Invoke-RestMethod -Uri 'http://localhost:8000/api/cmdlet' -Method 'post' -Body $body -ContentType "application/json"
}