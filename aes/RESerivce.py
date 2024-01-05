# az login
# az account set -s 006c31bd-51e0-41db-b622-d1d3f8e7213a
# az quantum workspace set -g AzureQuantum -w AQ-Demo -l westus -o table
import qsharp
import qsharp.azure
from Wrapper import SmartWideRijndaelWrapper

targets = qsharp.azure.connect(
    resourceId="/subscriptions/006c31bd-51e0-41db-b622-d1d3f8e7213a/resourceGroups/AzureQuantum/providers/Microsoft.Quantum/Workspaces/AQ-Demo",
    location="westus")
print(targets)

# qsharp.azure.target("microsoft.estimator")

# Estimates.Rijndael<QAES.SmartWide.Rijndael>("smart_wide = true - Nr = 10 - Nk = 4 - in_place mixcolumn", 
# true, 10, 4, true, free_swaps, "_128_in-place-MC");
# qsharp.azure.submit(SmartWideRijndaelWrapper)
# 330a465d-9a2c-4315-b556-0487134a920c succeeded 

result = qsharp.azure.output("330a465d-9a2c-4315-b556-0487134a920c")
print(result)