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
def insurance_math(money, percentage):
    insurance = money * percentage
    return math.ceil(insurance)
def rounding_hundreds(unrounded):
    rounded = math.ceil(unrounded / 100) * 100
    return rounded
def tax_not_discounted(base, tax_percentage):
    tax_without_discount = base * tax_percentage
    return math.ceil(tax_without_discount)
def discount(payer, invalidity_1, invalidity_2, ztp):
    total_discount = payer + invalidity_1 + invalidity_2 + ztp
    return total_discount
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

health_worker_percentage = 0.045
health_insurance = insurance_math(gross_wage, health_worker_percentage)

social_worker_percentage = 0.071
social_insurance = insurance_math(gross_wage, social_worker_percentage)

tax_base = rounding_hundreds(gross_wage)

tax_percentage = 0.15
tax_before_discounts = tax_not_discounted(tax_base, tax_percentage)

#slevy
tax_payer = 0
invalidity_1_2 = 0
invalidity_3 = 0
ztp = 0
discount_bool = input("Máte daňovou slevu? (ano/ne) ").lower()
if discount_bool == "ano":
    while True:
        discount_choice = input("Jakou daňovou slevu máte: \n 1) Poplatník \n 2) Invalidita 1. a 2. stupně \n 3) Invalidita 3. stupně \n 4) ZTP/P \n 5)nic z výše uvedeného / vše jsem již zadal/a ")
        if discount_choice == "1":
            tax_payer = 2570
        elif discount_choice == "2":
            invalidity_1_2 = 210
        elif discount_choice == "3":
            invalidity_3 = 420
        elif discount_choice == "4":
            ztp = 1345
        else:
            break
elif discount_bool == "ne":
    print("Dobře, přeskakuju")
else:
    print("Dobře, přeskakuju")
discounts = discount(tax_payer, invalidity_1_2, invalidity_3, ztp)

print("==========VÝPIS VŠECH POTŘEBNÝCH INFORMACÍ==========")
print("Základová mzda: "+str(worked_money))
print("Náhrady mzdy: "+str(vacation_money))
print("Prémie a odměny: "+str(true_reward))
print("==================================")
print("Hrubá mzda: "+str(gross_wage))
print("Zdravotní pojištění: "+str(health_insurance))
print("Sociální pojištění: "+str(social_insurance))
print("Základ daně: "+str(tax_base))
print("Daň před slevami: "+str(tax_before_discounts))
print("Slevy: "+str(discounts))
print("====================================================")