import math

def multi(factor1, factor2):
    return math.ceil(factor1 * factor2)
def hourly_rate(month_hours, monthly_pay):
    return monthly_pay / month_hours
def rounding_hundreds(unrounded):
    return math.ceil(unrounded / 100) * 100
def discount(payer, invalidity_1, invalidity_2, ztp):
    return payer + invalidity_1 + invalidity_2 + ztp
def multiple_kids_count(kids):
    return 5447 + (kids - 3) * 2320
def tax_after_discount(base, discounts):
    return max(0, base - discounts)
def tax_after_benefit(discounted, benefit):
    return discounted - benefit
def take_home_pay(gross, health, social, tax):
    return gross - health - social - tax

vacation_money = 0
true_reward = 0

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

worked_money = multi(worked_hours, basic_hourly_rate)
print("Základová mzda je "+str(worked_money)+" Kč")

vacation = input("Byl/a jste na dovolené?(ano/ne) ").lower()
if vacation == "ano":
    vacation_hours = int(input("Kolik hodin? "))
    vacation_hourly_rate = float(input("Jaká je Vaše náhradová mzda?(Kč/hod) "))
    vacation_money = multi(vacation_hours, vacation_hourly_rate)
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
        true_reward = multi(worked_money, rewards_percentage / 100)
    else:
        print("Neznám, pokračuju s nulovou odměnou/prémií")
elif rewards == "ne":
    print("Dobře, přeskakuju")
else:
    print("Takovou hodnotu neznám. Pokračuju s nulovou odměnou/prémií")

gross_wage = worked_money+vacation_money+true_reward

health_insurance = multi(gross_wage, 0.045)

social_insurance = multi(gross_wage, 0.071)

tax_base = rounding_hundreds(gross_wage)

tax_before_discounts = multi(tax_base,0.15)

# slevy
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

# daňové zvýhodnění
tax_benefit = 0
tax_benefits_bool = input("Máte daňové zvýhodnění? (ano/ne) ")
if tax_benefits_bool == "ano":
    kids_count = int(input("Kolik máte dětí? "))
    if kids_count == 1:
        tax_benefit = 1267
    elif kids_count == 2:
        tax_benefit = 3127
    elif kids_count == 3:
        tax_benefit = 5447
    elif kids_count > 3:
        tax_benefit = multiple_kids_count(kids_count)
elif tax_benefits_bool == "ne":
    print("Dobře, přeskakuju.")
else:
    print("Tento výraz neznám. Počítám s výchozí hodnotou 0")
# daň po slevách
tax_after_discount_checked = 0
tax_bonus = 0

tax_discount_only = tax_after_discount(tax_before_discounts, discounts)
tax_with_benefits = tax_after_benefit(tax_discount_only, tax_benefit)

if tax_with_benefits < 0:
    tax_bonus = abs(tax_with_benefits)
else:
    tax_after_discount_checked = tax_with_benefits

# čistá mzda
net_pay = take_home_pay(gross_wage, health_insurance, social_insurance, tax_after_discount_checked)

# doplatek
supplement = net_pay + tax_bonus

# zaměstnavatel pojištění
employer_health_insurance = multi(gross_wage, 0.09)
employer_social_insurance = multi(gross_wage, 0.248)

print("==========VÝPIS VŠECH POTŘEBNÝCH INFORMACÍ==========")
print(f"Základová mzda: {worked_money}")
print(f"Náhrady mzdy: {vacation_money}")
print(f"Prémie a odměny: {true_reward}")
print("==================================")
print(f"Hrubá mzda: {gross_wage}")
print(f"Zdravotní pojištění: {health_insurance}")
print(f"Sociální pojištění: {social_insurance}")
print(f"Základ daně: {tax_base}")
print(f"Daň před slevami: {tax_before_discounts}")
print(f"Slevy: {discounts}")
print(f"Daňové zvýhodnění: {tax_benefit}")
print(f"Daň po slevách: {tax_after_discount_checked}")
print(f"Čistá mzda: {net_pay}")
print(f"Daňový bonus: {tax_bonus}")
print(f"Doplatek k výplatě: {supplement}")
print("==================================")
print(f"Zdravotní pojištění zaměstnavatel: {employer_health_insurance}")
print(f"Sociální pojištění zaměstnavatel: {employer_social_insurance}")
print("====================================================")