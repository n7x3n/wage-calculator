function money_made(hours, hourly_rate){
    let calculated_money = hours * hourly_rate;
    return Math.ceil(calculated_money);
}
function premie(money, percentage){
    reward = money * (percentage/100);
    return Math.ceil(reward);
}
function insurance_math(money, percentage){
    insurance = money * percentage;
    return Math.ceil(insurance);
}
function rounding_hundreds(unrounded){
    rounded = Math.ceil(unrounded / 100) * 100;
    return rounded;
}
const hoursInput = document.getElementById("worked_hours");
const rateInput = document.getElementById("hourly_rate");
const vacHoursInput = document.getElementById("vacation_hours");
const vacRateInput = document.getElementById("vacation_rate");
const rewardInput = document.getElementById("rewards");
const health_percent = 0.045
const social_percent = 0.071
const tax_percent = 0.15
const premiumInput = document.getElementById("premium_percentage");
const calc_button = document.getElementById("calc_btn");

calc_button.addEventListener('click', () =>{
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
    premium = premium / 100;
    let true_premium = insurance_math(zakl_mzda, premium) || 0;
    let reward_premium = true_premium + reward || 0;
    let grosswage = zakl_mzda + vacation + reward_premium;
    let health_insur = insurance_math(grosswage, health_percent) || 0;
    let social_insur = insurance_math(grosswage, social_percent) || 0;
    let tax_base = rounding_hundreds(grosswage) || 0;
    let basic_tax = insurance_math(tax_base, tax_percent) || 0;
    document.getElementById('zakladova_mzda').innerText = zakl_mzda + " Kč";
    document.getElementById('nahrady_mzdy').innerText = vacation + " Kč";
    document.getElementById('premie_odmeny').innerText = reward_premium + " Kč";
    document.getElementById('hruba_mzda').innerText = grosswage + " Kč";
    document.getElementById('zdrav_poj').innerText = health_insur + " Kč";
    document.getElementById('soc_poj').innerText = social_insur + " Kč";
    document.getElementById('zakl_dan').innerText = tax_base + " Kč";
    document.getElementById('dan_pr_slev').innerText = basic_tax + " Kč";
});