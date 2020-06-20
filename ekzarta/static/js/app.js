const mq = window.matchMedia("(min-width: 1200px)");

if (mq.matches) {
  new fullpage("#fullpage", {
    autoScrolling: true,
    navigation: true,
    onLeave: (origin, destination, direction) => {
      const section = destination.item;
      const title = section.querySelector("h1");
      const tl = new TimelineMax({ delay: 0.5 });
      tl.fromTo(title, 0.5, { y: "50", opacity: 0 }, { y: 0, opacity: 1 });
      /*if (destination.index === 1) {
        const bottle = document.querySelector(".bottle");
        tl.fromTo(bottle, 0.7, { x: "100%" }, { x: "0%" });
      }*/
    }
  });
} else {
  new fullpage("#fullpage", {
    onLeave: (origin, destination, direction) => {
      const section = destination.item;
      const title = section.querySelector("h1");
      const tl = new TimelineMax({ delay: 0.5 });
      tl.fromTo(title, 0.5, { y: "50", opacity: 0 }, { y: 0, opacity: 1 });
      /*if (destination.index === 1) {
        const bottle = document.querySelector(".bottle");
        tl.fromTo(bottle, 0.7, { x: "100%" }, { x: "0%" });
      }*/
    }
  });
}

window.addEventListener("load", () => {
  const tl = new TimelineMax({ delay: 0.5 });
  const hero = document.querySelectorAll("main");

  tl.fromTo(hero, 0.5, { opacity: "0", x: "-20%" }, { x: "0%", opacity: "1" });
});
