import math

def money_made(hours, hourly_rate):
    calculated_money = hours * hourly_rate
    return math.ceil(calculated_money)
def hourly_rate(month_hours, monthly_pay):
    calculated_rate = monthly_pay / month_hours
    return calculated_rate
def premie(money, percentage):
    reward = money * (percentage/100)
    return math.ceil(reward)
####
vacation_money = 0
true_reward = 0
####
####
print("Ahoj. Tohle je mzdová kalkulačka. Postupně mi budete psát hodnoty a já Váma na konci spočítám celý výpis.")
worked_choice = input("Mám počítat podle 1) měsíčního platu nebo 2)podle hodinového mzdového tarifu?(1 nebo 2) ")
if worked_choice == "1":
    work_hours = int(input("kolik pracovních hodin má měsíc?(hod) "))
    worked_hours = int(input("Kolik hodin jste odpracoval/a?(hod) "))
    month_pay = int(input("Jakou máte měsíční mzdu? (Kč) ").replace(" ", ""))
    basic_hourly_rate = hourly_rate(work_hours, month_pay)

elif worked_choice == "2":
    worked_hours = int(input("Kolik hodin jste odpracoval/a?(hod) "))
    basic_hourly_rate = float(input("Jakou máte hodinovou mzdu? (Kč/hod) "))

else:
    print("Tuto hodnotu neznám. Automaticky počítám s hodinovým mzdovým tarifem")
    worked_hours = int(input("Kolik hodin jste odpracoval/a?(hod) "))
    basic_hourly_rate = float(input("Jakou máte hodinovou mzdu? (Kč/hod) "))


worked_money = money_made(worked_hours, basic_hourly_rate)
print("Základová mzda je "+str(worked_money)+" Kč")
# po tento pod to funguje =)

vacation = input("Byl/a jste na dovolené?(ano/ne) ").lower()
if vacation == "ano":
    vacation_hours = int(input("Kolik hodin? "))
    vacation_hourly_rate = float(input("Jaká je Vaše náhradová mzda?(Kč/hod) "))
    vacation_money = money_made(vacation_hours, vacation_hourly_rate)
elif vacation == "ne":
    print("Dobře, přeskakuju.")
else:
    print("Tuto hodnotu neznám. Počítám s žádnou dovolenou.")
print(vacation_money)

rewards = input("Byly odměny/prémie?(ano/ne) ")
if rewards == "ano":
    rewards_type = input("A byly to: \n1) odměny \n2) prémie?(1 nebo 2) ")
    if rewards_type == "1":
        true_reward = int(input("Kolik bylo v odměnách? ") .replace(" ", ""))
    elif rewards_type == "2":
        rewards_percentage = int(input("Kolik procent ze mzdy?(%) "))
        true_reward = premie(worked_money, rewards_percentage)
    else:
        print("Neznám, pokračuju s nulovou odměnou/prémií")
elif rewards == "ne":
    print("Dobře, přeskakuju")
else:
    print("Takovou hodnotu neznám. Pokračuju s nulovou odměnou/prémií")
gross_wage = worked_money+vacation_money+true_reward


print("==========VÝPIS VŠECH POTŘEBNÝCH INFORMACÍ==========")
print("Základová mzda: "+str(worked_money))
print("Náhrady mzdy: "+str(vacation_money))
print("Prémie a odměny: "+str(true_reward))
print("==================================")
print("Hrubá mzda: "+str(gross_wage))
print("====================================================")