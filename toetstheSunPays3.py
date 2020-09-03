#%% 
# Hierdie bladsy toets die battery module wat die theSunPays 4.8kWh 
# battery lees.

# Trek in die module van die battery
import sunpays4_8kWbattery

#%% 
# Lees 'n lyn van die battery en druk dit
statuslyn = leesStatusBattery()
print(statuslyn)


#%%
# Lees die SOC van die battery en druk dit
SOC = leesSOCBattery()
print(SOC)