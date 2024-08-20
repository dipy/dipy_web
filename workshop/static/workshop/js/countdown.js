function getTimeRemaining(endtime) {
  let t = Date.parse(endtime) - Date.parse(new Date());
  let seconds = Math.floor((t / 1000) % 60);
  let minutes = Math.floor((t / 1000 / 60) % 60);
  let hours = Math.floor((t / (1000 * 60 * 60)) % 24);
  let days = Math.floor(t / (1000 * 60 * 60 * 24));
  return {
    total: t,
    days: days,
    hours: hours,
    minutes: minutes,
    seconds: seconds,
  };
}

function initializeClock(id, startTime, endTime, enable) {
  let clockStop = document.getElementById(id + "-stop");
  let clock = document.getElementById(id);
  let enableBlock = enable.map((e) => document.getElementById(e));
  let clockTitle = document.getElementById(id + "-title");
  let daysSpan = clock.querySelector(".days");
  let hoursSpan = clock.querySelector(".hours");
  let minutesSpan = clock.querySelector(".minutes");
  let secondsSpan = clock.querySelector(".seconds");
  if (startTime == 0) {
    clock.style.display = "flex";
    clockTitle.style.display = "block";
    enableBlock.forEach((e) => (e.style.display = "none"));
  }

  let timeinterval = setInterval(updateClock, 1000);

  function updateClock() {
    let t = getTimeRemaining(endTime);

    daysSpan.innerHTML = t.days;
    hoursSpan.innerHTML = ("0" + t.hours).slice(-2);
    minutesSpan.innerHTML = ("0" + t.minutes).slice(-2);
    secondsSpan.innerHTML = ("0" + t.seconds).slice(-2);

    if (startTime != 0 && getTimeRemaining(startTime).total <= 0) {
      clock.style.display = "flex";
      clockTitle.style.display = "block";
      enableBlock.forEach((e) => (e.style.display = "none"));
    }
    if (t.total <= 0) {
      clearInterval(timeinterval);
      clock.style.display = "none";
      clockTitle.style.display = "none";
      clockStop.style.display = "block";
      enableBlock.forEach((e) => (e.style.display = "block"));
    }
  }
}

const workshopStart = "2025-03-17T09:00:00-04:00";
const registrationStart = "2024-08-29T09:00:00-04:00";
initializeClock("countdown", registrationStart, workshopStart, []);
initializeClock("reg-countdown", 0, registrationStart, [
  "Registration",
  "Registration-link",
]);
