$commonParams = @(
    "Debug",
    "ErrorAction",
    "ErrorVariable",
    "InformationAction",
    "InformationVariable",
    "OutVariable",
    "OutBuffer",
    "PipelineVariable",
    "Verbose",
    "WarningAction",
    "WarningVariable",
    "WhatIf",
    "Confirm"
)

$cmdlets = Get-Command -Module AzureRM

$results = New-Object System.Collections.ArrayList
foreach ($cmdlet in $cmdlets) {
    if ($cmdlet.ParameterSets.Count -gt 1) {
        foreach ($parameterSet in $cmdlet.ParameterSets) {
            foreach ($prameter in $parameterSet.Parameters) {
                if ($prameter.Name -notin $commonParams) {
                    $body = @{
                        'name' = $cmdlet.Name;
                        'parameter' = $prameter.Name;
                        'parameter_type' = $prameter.ParameterType.FullName;
                        'parameter_set' = $parameterSet.Name
                    }
                    $null = $results.Add($body)
                }
            }
        }
    } else {
        foreach ($paramKey in $cmdlet.Parameters.Keys) {
            if ($paramKey -notin $commonParams) {
                $body = @{
                    'name' = $cmdlet.Name;
                    'parameter' = $cmdlet.Parameters[$paramKey].Name;
                    'parameter_type' = $cmdlet.Parameters[$paramKey].ParameterType.FullName;
                    'parameter_set' = '__AllParameterSets'
                }
                $null = $results.Add($body)
            }
        }
    }
}

foreach ($result in $results) {
    $percentage = $results.IndexOf($result) / $results.Count * 100
    Write-Progress  -Activity 'Updating parameters ...' -CurrentOperation $result['name'] -PercentComplete $percentage

    $body = ConvertTo-Json $result
    $null = Invoke-RestMethod -Uri 'http://localhost:8000/api/cmdletparameter' -Method 'post' -Body $body -ContentType "application/json"
}