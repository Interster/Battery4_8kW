#%% 
# Hierdie bladsy toets die battery module wat die theSunPays 4.8kWh 
# battery lees.

# Trek in die module van die battery
import sunpays4_8kWbattery as bat

#%% 
# Lees 'n lyn van die battery en druk dit
statuslyn = bat.leesStatusBattery()
print(statuslyn)


#%%
# Lees die SOC van die battery en druk dit
SOC = bat.leesSOCBattery()
print(SOC*100)

# %%
# Te doen:
# Maak nou module van die Axpert wat opdragte daarnatoe kan stuur
# Een van opdragte is gaan na SBU
#
# Skryf dan 'n program wat kyk wat SOC is en as dit laer as 'n 
# sekere waarde is, verander Axpert na lynkrag toe
# Dan verander alle modules dat die Axpert en battery objekte is