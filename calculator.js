function money_made(hours, hourly_rate) {
    let calculated_money = hours * hourly_rate;
    return Math.ceil(calculated_money);
}
function premie(money, percentage) {
    reward = money * (percentage / 100);
    return Math.ceil(reward);
}
function insurance_math(money, percentage) {
    insurance = money * percentage;
    return Math.ceil(insurance);
}
function rounding_hundreds(unrounded) {
    rounded = Math.ceil(unrounded / 100) * 100;
    return rounded;
}
function discount(payer, invalidity_1, invalidity_2, ztp) {
    total_discount = payer + invalidity_1 + invalidity_2 + ztp;
    return total_discount;
}
function multiple_kids_count(kids) {
    benefit = 5447 + (kids - 3) * 2320;
    return benefit;
}
function tax_after_discount(base, discounts) {
    discounted = base - discounts;
    if (discounted < 0) {
        discounted = 0;
    } else {
        discounted = discounted;
    }
    return discounted;
}
function tax_after_benefit(discounted, benefit) {
    final = discounted - benefit;
    return final;
}
function take_home_pay(gross, health, social, tax) {
    net = gross - health - social - tax;
    return net;
}
const hoursInput = document.getElementById("worked_hours");
const rateInput = document.getElementById("hourly_rate");
const vacHoursInput = document.getElementById("vacation_hours");
const vacRateInput = document.getElementById("vacation_rate");
const rewardInput = document.getElementById("rewards");
//předdefinované hodnoty
const health_percent = 0.045;
const social_percent = 0.071;
const tax_percent = 0.15;
const emp_health_per = 0.09;
const emp_soc_per = 0.248;
//
const payerInput = document.getElementById("payer");
const inv1_2Input = document.getElementById("inv1_2");
const inv3Input = document.getElementById("inv3");
const ztpInput = document.getElementById("ztp");
const premiumInput = document.getElementById("premium_percentage");
const benefitInput = document.getElementById("tax_benefits");
const calc_button = document.getElementById("calc_btn");

calc_button.addEventListener('click', () => {
    let hours = parseInt(hoursInput.value) || 0;
    let rate = parseFloat(rateInput.value) || 0;
    let zakl_mzda = money_made(hours, rate);
    let vacHours = parseInt(vacHoursInput.value) || 0;
    let vacRate = parseFloat(vacRateInput.value) || 0;
    let vacation = money_made(vacHours, vacRate);
    let reward = parseInt(rewardInput.value) || 0;
    if (reward <= 0) {
        reward = 0
    } else {
        reward = reward
    }
    let premium = parseInt(premiumInput.value) || 0;
    let true_premium = premie(zakl_mzda, premium) || 0;
    let reward_premium = true_premium + reward || 0;
    let grosswage = zakl_mzda + vacation + reward_premium;
    let health_insur = insurance_math(grosswage, health_percent) || 0;
    let social_insur = insurance_math(grosswage, social_percent) || 0;
    let tax_base = rounding_hundreds(grosswage) || 0;
    let basic_tax = insurance_math(tax_base, tax_percent) || 0;
    let tax_payer = 0;
    let invalidity_1_2 = 0;
    let invalidity_3 = 0;
    let ztp = 0;
    if (payerInput.checked) {
        tax_payer = 2570;
    }
    if (inv1_2Input.checked) {
        invalidity_1_2 = 210;
    }
    if (inv3Input.checked) {
        invalidity_3 = 420;
    }
    if (ztpInput.checked) {
        ztp = 1345;
    }
    let discounts = discount(tax_payer, invalidity_1_2, invalidity_3, ztp) || 0;
    let benefit = 0;
    let kids_count = parseInt(benefitInput.value) || 0;
    if (kids_count == 1) {
        benefit = 1267;
    } else if (kids_count == 2) {
        benefit = 3127;
    } else if (kids_count == 3) {
        benefit = 5447;
    } else if (kids_count > 3) {
        benefit = multiple_kids_count(kids_count);
    }
    let discounted_tax = tax_after_discount(basic_tax, discounts);
    let final_tax = tax_after_benefit(discounted_tax, benefit);
    let final_tax_checked = 0;
    let tax_bonus = 0;
    if (final_tax < 0) {
        tax_bonus = -final_tax;
        final_tax_checked = 0;
    } else {
        final_tax_checked = final_tax;
    }
    let net_pay = take_home_pay(grosswage, health_insur, social_insur, final_tax_checked);
    let supplement = net_pay + tax_bonus;
    let emp_health_insur = insurance_math(grosswage, emp_health_per);
    let emp_soc_insur = insurance_math(grosswage, emp_soc_per);
    document.getElementById('dan_zvyh').innerText = benefit + " Kč";
    document.getElementById('zakladova_mzda').innerText = zakl_mzda + " Kč";
    document.getElementById('nahrady_mzdy').innerText = vacation + " Kč";
    document.getElementById('premie_odmeny').innerText = reward_premium + " Kč";
    document.getElementById('hruba_mzda').innerText = grosswage + " Kč";
    document.getElementById('zdrav_poj').innerText = health_insur + " Kč";
    document.getElementById('soc_poj').innerText = social_insur + " Kč";
    document.getElementById('zakl_dan').innerText = tax_base + " Kč";
    document.getElementById('dan_pr_slev').innerText = basic_tax + " Kč";
    document.getElementById('slevy').innerText = discounts + " Kč";
    document.getElementById('dan_zvyh').innerText = benefit + " Kč";
    document.getElementById('dan_po_slev').innerText = final_tax_checked + " Kč";
    document.getElementById('cis_mzda').innerText = net_pay + " Kč";
    document.getElementById('dan_bon').innerText = tax_bonus + " Kč";
    document.getElementById('dop_vyp').innerText = supplement + " Kč";
    document.getElementById('zdrav_poj_zam').innerText = emp_health_insur + " Kč";
    document.getElementById('soc_poj_zam').innerText = emp_soc_insur + " Kč";
});