$cmdlets = Get-Command -Module AzureRM

$results = New-Object System.Collections.ArrayList
foreach ($cmdlet in $cmdlets) {
    if ($cmdlet.OutputType) {
        foreach ($outputType in $cmdlet.OutputType) {
            $body = @{
                'name' = $cmdlet.Name;
                'output_type' = $outputType.Name
            }
            $null = $results.Add($body)
        }
    }
}

foreach ($result in $results) {
    $percentage = $results.IndexOf($result) / $results.Count * 100
    Write-Progress  -Activity 'Updating outputtypes ...' -CurrentOperation $result['name'] -PercentComplete $percentage

    $body = ConvertTo-Json $result
    $null = Invoke-RestMethod -Uri 'http://localhost:8000/api/cmdletoutputtype' -Method 'post' -Body $body -ContentType "application/json"
}