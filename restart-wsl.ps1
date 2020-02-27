$ServiceName = 'LxssManager'
$arrService = Get-Service -Name $ServiceName

while ($arrService.Status -ne 'Stopped')
{
    Stop-Service $ServiceName
    Write-Host $arrService.status
    Write-Host 'Stopping ...'
    Start-Sleep -seconds 60

    $arrService.Refresh()

    if ($arrService.Status -eq 'Stopped')
    {
        Write-Host 'Service is now stopped.'
    }
}

while ($arrService.Status -ne 'Running')
{
    Start-Service $ServiceName
    Write-Host $arrService.status
    Write-Host 'Starting ...'
    Start-Sleep -seconds 60
    $arrService.Refresh()
    if ($arrService.Status -eq 'Running')
    {
        Write-Host 'Service is now running.'
    }
}
