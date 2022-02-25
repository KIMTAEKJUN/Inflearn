const API_KEY = "e7c7a639b28c96f82e3d95a253fcdc1b";

const temp = document.querySelector("#temp");
const t1 = temp.querySelectorAll("span")[0];
const t2 = temp.querySelectorAll("span")[1];
const t3 = temp.querySelectorAll("span")[2];

const city = document.querySelector("#city");
const KR = city.querySelectorAll("span")[0];
const Region = city.querySelectorAll("span")[1];
const weatherCondition = city.querySelectorAll("span")[2];

function onGeoOk(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            // 오늘 온도, 최고 온도, 최저 온도
            const temp = data.main.temp;
            const maxTemp = data.main.temp_max;
            const minTemp = data.main.temp_min;

            // 나라, 지역, 날씨
            const kr = data.sys.country;
            const region = data.name;
            const weather = data.weather[0].main;

            t1.innerText = `오늘 온도 : ${temp.toFixed(1)}°`;
            t2.innerText = `최고 온도 : ${maxTemp.toFixed(1)}°`;
            t3.innerText = `최저 온도 : ${minTemp.toFixed(1)}°`;

            KR.innerText = `나라 : ${kr}`;
            Region.innerText = `지역 : ${region}`
            weatherCondition.innerText = `날씨 : ${weather}`
    });
}
function onGeoError() {
    alert("Can't find you, No weather for you.");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);