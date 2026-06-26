function money_made(hours, hourly_rate){
    let calculated_money = hours * hourly_rate;
    return Math.ceil(calculated_money);
}
function premie(money, percentage){
    reward = money * (percentage/100)
    return Math.ceil(reward)
}
function insurance_math(money, percentage){
    insurance = money * percentage
    return Math.ceil(insurance)
}
function rounding_hundreds(unrounded){
    rounded = Math.ceil(unrounded / 100) * 100
}
const hoursInput = document.getElementById("worked_hours");
const rateInput = document.getElementById("hourly_rate");
const calc_button = document.getElementById("calc_btn");

calc_button.addEventListener('click', () =>{
    let hours = parseInt(hoursInput.value);
    let rate = parseInt(rateInput.value);
    let result = money_made(hours, rate);
    document.getElementById('zakladova_mzda').innerText = result + " Kč";
});