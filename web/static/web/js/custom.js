  document.getElementById("year").textContent = new Date().getFullYear();

    // Back to Top Button
  const backToTopBtn = document.getElementById("backToTopBtn");

  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 300) {
      backToTopBtn.style.display = "flex";
      backToTopBtn.style.justifyContent = "center";
      backToTopBtn.style.alignItems = "center";
    } else {
      backToTopBtn.style.display = "none";
    }
  });

  backToTopBtn.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  // Sticky Navbar
  const navbarWrapper = document.getElementById("navbarWrapper");
  window.addEventListener("scroll", function () {
    if (window.scrollY > 50) {
      navbarWrapper.classList.add("sticky");
    } else {
      navbarWrapper.classList.remove("sticky");
    }
  });

  // Number Counting Animation
  document.addEventListener("DOMContentLoaded", function () {
    const startAnimation = (counter) => {
      const target = +counter.getAttribute("data-target");
      const duration = 2000; // 2 seconds
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const value = Math.floor(progress * target);

        counter.textContent = value.toLocaleString();

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        }
      };

      requestAnimationFrame(updateCount);
    };

    // Intersection Observer setup
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            startAnimation(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    document.querySelectorAll(".counter").forEach((counter) => {
      observer.observe(counter);
    });
  });

  // Marquee Animation
  document.addEventListener("DOMContentLoaded", function () {
    const marquee = document.querySelector(".marquee-vertical");
    if (marquee) {
      const list = marquee.querySelector("ul");
      const items = list.querySelectorAll("li");
      const containerHeight = 200; // Match your container height

      // Clone the first item and append to end if not already appended
      if (!list.lastElementChild.isEqualNode(items[0])) {
        const firstItem = items[0].cloneNode(true);
        list.appendChild(firstItem);
      }

      // Reset position when animation completes
      marquee.addEventListener("animationiteration", function () {
        // Briefly pause to allow reset
        marquee.style.animation = "none";
        setTimeout(() => {
          marquee.style.animation = "marqueeVertical 30s linear infinite";
        }, 10);
      });
    }
  });

  // Navbar Toggler Icons
  document.addEventListener("DOMContentLoaded", function () {
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.getElementById("navbarNav");

    // Initialize icons based on current state
    function initializeIcons() {
      const togglerIcon = navbarToggler.querySelector(
        ".navbar-toggler-icon"
      );
      const closeIcon = navbarToggler.querySelector(".close-icon");

      if (navbarCollapse.classList.contains("show")) {
        togglerIcon.classList.add("d-none");
        closeIcon.classList.remove("d-none");
      } else {
        togglerIcon.classList.remove("d-none");
        closeIcon.classList.add("d-none");
      }
    }

    // Set initial state
    initializeIcons();

    // Handle collapse events
    navbarCollapse.addEventListener("show.bs.collapse", function () {
      const togglerIcon = navbarToggler.querySelector(
        ".navbar-toggler-icon"
      );
      const closeIcon = navbarToggler.querySelector(".close-icon");

      togglerIcon.style.transition = "none";
      closeIcon.style.transition = "none";

      togglerIcon.classList.add("d-none");
      closeIcon.classList.remove("d-none");

      // Force reflow to ensure the transition is applied
      void togglerIcon.offsetWidth;
      void closeIcon.offsetWidth;

      togglerIcon.style.transition = "";
      closeIcon.style.transition = "";
    });

    navbarCollapse.addEventListener("hide.bs.collapse", function () {
      const togglerIcon = navbarToggler.querySelector(
        ".navbar-toggler-icon"
      );
      const closeIcon = navbarToggler.querySelector(".close-icon");

      togglerIcon.style.transition = "none";
      closeIcon.style.transition = "none";

      togglerIcon.classList.remove("d-none");
      closeIcon.classList.add("d-none");

      // Force reflow to ensure the transition is applied
      void togglerIcon.offsetWidth;
      void closeIcon.offsetWidth;

      togglerIcon.style.transition = "";
      closeIcon.style.transition = "";
    });

    // Handle dropdown hover behavior
    function setupDropdownHover() {
      const isMobile = window.innerWidth < 992;
      const dropdowns = document.querySelectorAll(".nav-item.dropdown");

      dropdowns.forEach((dropdown) => {
        if (!isMobile) {
          dropdown.addEventListener("mouseenter", function () {
            const menu = this.querySelector(".dropdown-menu");
            if (menu) {
              menu.style.display = "block";
              setTimeout(() => {
                menu.style.opacity = "1";
                menu.style.visibility = "visible";
              }, 10);
            }
          });

          dropdown.addEventListener("mouseleave", function () {
            const menu = this.querySelector(".dropdown-menu");
            if (menu) {
              menu.style.opacity = "0";
              menu.style.visibility = "hidden";
              setTimeout(() => {
                menu.style.display = "none";
              }, 300);
            }
          });
        }
      });
    }

    // Initialize and update on resize
    setupDropdownHover();
    window.addEventListener("resize", setupDropdownHover);
  });
  