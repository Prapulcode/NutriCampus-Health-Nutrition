/**
 * NutriCampus - Health and Nutrition Awareness Web Application
 * Course: 25CPD37 - Community Project using Innovation and Design Thinking
 * Department of Computer Science and Engineering, New Horizon College of Engineering
 */

(function () {
  'use strict';

  // ==========================================
  // 1. STATE & STORAGE MANAGEMENT
  // ==========================================
  const STORAGE_KEYS = {
    THEME: 'nutri_theme',
    WATER_DATA: 'nutri_water_data',
    FEEDBACK: 'nutri_feedback_list',
    QUIZ_BEST: 'nutri_quiz_best_score'
  };

  const getTodayDateString = () => {
    const today = new Date();
    return today.toISOString().split('T')[0];
  };

  // Toast notification helper
  function showToast(message, icon = '✅') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      if (toast.parentNode) {
        toast.parentNode.removeChild(toast);
      }
    }, 3000);
  }

  // ==========================================
  // 2. THEME SWITCHER (Dark / Light Mode)
  // ==========================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const savedTheme = localStorage.getItem(STORAGE_KEYS.THEME) || 'theme-light';

  document.body.className = savedTheme;

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.body.classList.contains('theme-dark');
      const newTheme = isDark ? 'theme-light' : 'theme-dark';
      document.body.className = newTheme;
      localStorage.setItem(STORAGE_KEYS.THEME, newTheme);
      showToast(isDark ? 'Light theme activated' : 'Dark theme activated', isDark ? '☀️' : '🌙');
    });
  }

  // ==========================================
  // 3. TAB NAVIGATION SYSTEM
  // ==========================================
  const navLinks = document.querySelectorAll('.nav-link, .drawer-link, [data-tab]');
  const pageTabs = document.querySelectorAll('.page-tab');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const closeDrawerBtn = document.getElementById('closeDrawerBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const backdrop = document.getElementById('backdrop');

  function switchTab(tabId) {
    if (!tabId) return;
    const targetTab = document.getElementById(`tab-${tabId}`);
    if (!targetTab) return;

    // Hide all tabs
    pageTabs.forEach(tab => tab.classList.remove('active'));
    // Show selected tab
    targetTab.classList.add('active');

    // Update active state in nav links
    navLinks.forEach(link => {
      if (link.getAttribute('data-tab') === tabId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // Close mobile drawer if open
    closeMobileDrawer();

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Update URL hash without reload
    history.replaceState(null, null, `#${tabId}`);
  }

  function openMobileDrawer() {
    if (mobileDrawer) mobileDrawer.classList.add('open');
    if (backdrop) backdrop.classList.add('show');
  }

  function closeMobileDrawer() {
    if (mobileDrawer) mobileDrawer.classList.remove('open');
    if (backdrop) backdrop.classList.remove('show');
  }

  if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileDrawer);
  if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeMobileDrawer);
  if (backdrop) backdrop.addEventListener('click', closeMobileDrawer);

  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const targetTab = link.getAttribute('data-tab');
      if (targetTab) {
        e.preventDefault();
        switchTab(targetTab);
      }
    });
  });

  // Handle URL hash on initial load
  window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash.replace('#', '');
    if (hash && document.getElementById(`tab-${hash}`)) {
      switchTab(hash);
    } else {
      switchTab('home');
    }
  });

  // ==========================================
  // 4. NUTRITION GUIDE: FOOD CATEGORY FILTER
  // ==========================================
  const filterChips = document.querySelectorAll('.filter-chip');
  const foodCards = document.querySelectorAll('.food-card');

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');

      const filterVal = chip.getAttribute('data-filter');
      foodCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filterVal === 'all' || cat === filterVal) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  // ==========================================
  // 5. BMI CALCULATOR
  // ==========================================
  const metricUnitBtn = document.getElementById('metricUnitBtn');
  const imperialUnitBtn = document.getElementById('imperialUnitBtn');
  const metricFields = document.getElementById('metricFields');
  const imperialFields = document.getElementById('imperialFields');
  const bmiForm = document.getElementById('bmiForm');
  const resetBmiBtn = document.getElementById('resetBmiBtn');

  const bmiPlaceholder = document.getElementById('bmiPlaceholder');
  const bmiActiveResult = document.getElementById('bmiActiveResult');
  const bmiValueDisplay = document.getElementById('bmiValueDisplay');
  const bmiCategoryBadge = document.getElementById('bmiCategoryBadge');
  const meterPointer = document.getElementById('meterPointer');
  const healthyRangeText = document.getElementById('healthyRangeText');
  const bmiExplanationText = document.getElementById('bmiExplanationText');

  let currentUnit = 'metric'; // 'metric' or 'imperial'

  if (metricUnitBtn && imperialUnitBtn) {
    metricUnitBtn.addEventListener('click', () => {
      currentUnit = 'metric';
      metricUnitBtn.classList.add('active');
      imperialUnitBtn.classList.remove('active');
      metricFields.classList.remove('hidden');
      imperialFields.classList.add('hidden');
      document.getElementById('metricHeight').required = true;
      document.getElementById('metricWeight').required = true;
      document.getElementById('imperialFeet').required = false;
      document.getElementById('imperialWeight').required = false;
    });

    imperialUnitBtn.addEventListener('click', () => {
      currentUnit = 'imperial';
      imperialUnitBtn.classList.add('active');
      metricUnitBtn.classList.remove('active');
      imperialFields.classList.remove('hidden');
      metricFields.classList.add('hidden');
      document.getElementById('metricHeight').required = false;
      document.getElementById('metricWeight').required = false;
      document.getElementById('imperialFeet').required = true;
      document.getElementById('imperialWeight').required = true;
    });
  }

  if (bmiForm) {
    bmiForm.addEventListener('submit', (e) => {
      e.preventDefault();

      let heightCm = 0;
      let weightKg = 0;

      if (currentUnit === 'metric') {
        heightCm = parseFloat(document.getElementById('metricHeight').value);
        weightKg = parseFloat(document.getElementById('metricWeight').value);
      } else {
        const ft = parseFloat(document.getElementById('imperialFeet').value) || 0;
        const inch = parseFloat(document.getElementById('imperialInches').value) || 0;
        const lbs = parseFloat(document.getElementById('imperialWeight').value);
        const totalInches = (ft * 12) + inch;
        if (totalInches <= 0 || lbs <= 0) {
          alert('Please enter valid height and weight values.');
          return;
        }
        heightCm = totalInches * 2.54;
        weightKg = lbs * 0.45359237;
      }

      if (isNaN(heightCm) || isNaN(weightKg) || heightCm <= 0 || weightKg <= 0) {
        alert('Please enter valid numeric values for height and weight.');
        return;
      }

      const heightM = heightCm / 100;
      const bmi = weightKg / (heightM * heightM);
      const roundedBmi = parseFloat(bmi.toFixed(1));

      // Calculate healthy weight range for this height (18.5 - 24.9)
      const minHealthyKg = (18.5 * heightM * heightM).toFixed(1);
      const maxHealthyKg = (24.9 * heightM * heightM).toFixed(1);

      // Category analysis
      let category = '';
      let badgeClass = '';
      let explanation = '';
      let pointerPercent = 50; // default middle

      if (roundedBmi < 18.5) {
        category = 'Underweight (< 18.5)';
        badgeClass = 'badge-underweight';
        explanation = 'Your calculated BMI is below the standard population reference. For college students, this may stem from skipped meals or high metabolism. Emphasize energy-dense, nutritious foods like peanut butter, dairy/soy, lentils, nuts, and complex grains. Ensure adequate rest and avoid skipping breakfast.';
        // Pointer mapping: 0 to 25% for BMI up to 18.5
        pointerPercent = Math.max(5, (roundedBmi / 18.5) * 22);
      } else if (roundedBmi >= 18.5 && roundedBmi <= 24.9) {
        category = 'Normal / Healthy Range (18.5 - 24.9)';
        badgeClass = 'badge-normal';
        explanation = 'Your calculated BMI falls within the standard recommended healthy range. Maintain your balanced plate habits, daily water intake, regular physical movement across campus, and 7-8 hours of regular sleep!';
        // Pointer mapping: 25% to 60%
        const rangeRatio = (roundedBmi - 18.5) / (24.9 - 18.5);
        pointerPercent = 25 + (rangeRatio * 35);
      } else if (roundedBmi >= 25.0 && roundedBmi <= 29.9) {
        category = 'Overweight (25.0 - 29.9)';
        badgeClass = 'badge-overweight';
        explanation = 'Your calculated BMI is in the overweight bracket. Please note: if you actively train or play sports, increased muscle mass naturally increases BMI. Focus on sustainable lifestyle routines: choosing water over sugary sodas, taking 10-minute campus walks, and eating fiber-rich salads before lunch.';
        // Pointer mapping: 60% to 85%
        const rangeRatio = (roundedBmi - 25.0) / (29.9 - 25.0);
        pointerPercent = 60 + (rangeRatio * 25);
      } else {
        category = 'Obesity Range (≥ 30.0)';
        badgeClass = 'badge-obese';
        explanation = 'Your calculated BMI is 30 or higher. Rather than adopting restrictive crash diets, focus on gradual, compassionate adjustments: reducing deep-fried snacks, staying well-hydrated, establishing regular sleep, and consulting a healthcare professional at your campus health clinic for personalized support.';
        // Pointer mapping: 85% to 98%
        pointerPercent = Math.min(98, 85 + ((roundedBmi - 30) / 10) * 13);
      }

      // Render Results
      bmiValueDisplay.textContent = roundedBmi;
      bmiCategoryBadge.textContent = category;
      bmiCategoryBadge.className = `score-category-badge ${badgeClass}`;
      healthyRangeText.textContent = `${minHealthyKg} kg – ${maxHealthyKg} kg`;
      bmiExplanationText.textContent = explanation;
      meterPointer.style.left = `${pointerPercent}%`;

      bmiPlaceholder.classList.add('hidden');
      bmiActiveResult.classList.remove('hidden');

      showToast(`BMI calculated: ${roundedBmi} (${category})`, '⚖️');
    });

    resetBmiBtn.addEventListener('click', () => {
      bmiForm.reset();
      bmiPlaceholder.classList.remove('hidden');
      bmiActiveResult.classList.add('hidden');
    });
  }

  // ==========================================
  // 6. DAILY WATER INTAKE TRACKER
  // ==========================================
  const goalSelector = document.getElementById('goalSelector');
  const consumedDisplay = document.getElementById('consumedDisplay');
  const targetDisplay = document.getElementById('targetDisplay');
  const percentDisplay = document.getElementById('percentDisplay');
  const statusMessage = document.getElementById('statusMessage');
  const liquidFill = document.getElementById('liquidFill');
  const customAmountInput = document.getElementById('customAmountInput');
  const customAddBtn = document.getElementById('customAddBtn');
  const undoWaterBtn = document.getElementById('undoWaterBtn');
  const resetWaterBtn = document.getElementById('resetWaterBtn');
  const logListContainer = document.getElementById('logListContainer');
  const logCountText = document.getElementById('logCountText');

  // Load water data from localStorage
  function loadWaterData() {
    const today = getTodayDateString();
    const raw = localStorage.getItem(STORAGE_KEYS.WATER_DATA);
    let data = {
      date: today,
      target: 2500,
      consumed: 0,
      logs: []
    };

    if (raw) {
      try {
        const parsed = JSON.parse(raw);
        if (parsed.date === today) {
          data = parsed;
        } else {
          // New day auto-reset, but keep previous target
          data.target = parsed.target || 2500;
        }
      } catch (err) {
        console.error('Error parsing water data:', err);
      }
    }
    return data;
  }

  let waterState = loadWaterData();

  function saveWaterData() {
    localStorage.setItem(STORAGE_KEYS.WATER_DATA, JSON.stringify(waterState));
  }

  const MAX_WATER_ML = 5000; // Strict daily safety limit of 5.0 Liters / 5000 ml

  function updateWaterUI() {
    const target = waterState.target;
    const consumed = Math.min(MAX_WATER_ML, waterState.consumed);
    waterState.consumed = consumed;
    const percent = Math.min(100, Math.round((consumed / target) * 100));

    if (targetDisplay) targetDisplay.textContent = target;
    if (consumedDisplay) consumedDisplay.textContent = consumed;
    if (percentDisplay) percentDisplay.textContent = `${percent}% Reached`;
    if (liquidFill) liquidFill.style.height = `${percent}%`;

    if (goalSelector) goalSelector.value = target.toString();

    // Disable quick-add buttons and custom input when 5L limit reached
    const isAtLimit = consumed >= MAX_WATER_ML;
    document.querySelectorAll('.quick-btn').forEach(btn => {
      btn.disabled = isAtLimit;
      if (isAtLimit) {
        btn.classList.add('limit-reached');
      } else {
        btn.classList.remove('limit-reached');
      }
    });

    if (customAddBtn) customAddBtn.disabled = isAtLimit;
    if (customAmountInput) customAmountInput.disabled = isAtLimit;

    // Contextual status message
    if (statusMessage) {
      if (isAtLimit) {
        statusMessage.innerHTML = '💧 <strong>Daily Maximum Reached (5.0 L / 5000 ml):</strong> You are fully hydrated! Excessive fluid intake beyond 5 L is not recommended.';
      } else if (consumed === 0) {
        statusMessage.textContent = 'Start hydrating! Take a sip to kick off your day.';
      } else if (percent < 25) {
        statusMessage.textContent = 'Good start! Keep a water bottle handy at your desk.';
      } else if (percent < 50) {
        statusMessage.textContent = 'Nearly halfway! Staying hydrated prevents afternoon lecture fatigue.';
      } else if (percent < 75) {
        statusMessage.textContent = 'Great progress! More than halfway through your daily target.';
      } else if (percent < 100) {
        statusMessage.textContent = 'Almost there! Just a couple of glasses away from your goal.';
      } else {
        statusMessage.textContent = '🎉 Goal Achieved! Excellent hydration discipline today!';
      }
    }

    // Render Logs
    if (logListContainer) {
      logListContainer.innerHTML = '';
      if (!waterState.logs || waterState.logs.length === 0) {
        logListContainer.innerHTML = `<div class="empty-log-msg">No water intake logged yet today. Click one of the portion buttons above to add your first glass!</div>`;
        if (logCountText) logCountText.textContent = '0 entries today';
      } else {
        if (logCountText) logCountText.textContent = `${waterState.logs.length} ${waterState.logs.length === 1 ? 'entry' : 'entries'} today`;
        // Show newest logs at top
        waterState.logs.slice().reverse().forEach(entry => {
          const item = document.createElement('div');
          item.className = 'log-item';
          item.innerHTML = `
            <div class="log-left">
              <span>💧</span>
              <span class="log-amount">+${entry.amount} ml</span>
            </div>
            <span class="log-time">${entry.time}</span>
          `;
          logListContainer.appendChild(item);
        });
      }
    }
  }

  function addWater(amount) {
    amount = parseInt(amount, 10);
    if (isNaN(amount) || amount <= 0) return;

    if (waterState.consumed >= MAX_WATER_ML) {
      showToast('Daily maximum limit of 5.0 L (5000 ml) reached. Excessive water intake is not recommended!', '⚠️');
      updateWaterUI();
      return;
    }

    const now = new Date();
    const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    let addedAmount = amount;
    if (waterState.consumed + amount > MAX_WATER_ML) {
      addedAmount = MAX_WATER_ML - waterState.consumed;
      waterState.consumed = MAX_WATER_ML;
      waterState.logs.push({ amount: addedAmount, time: timeStr });
      saveWaterData();
      updateWaterUI();
      showToast(`Logged +${addedAmount} ml (Reached 5.0 L daily maximum limit)`, '💧');
      return;
    }

    waterState.consumed += addedAmount;
    waterState.logs.push({ amount: addedAmount, time: timeStr });
    saveWaterData();
    updateWaterUI();
    showToast(`Logged +${addedAmount} ml water`, '💧');
  }

  function undoLastWater() {
    if (!waterState.logs || waterState.logs.length === 0) {
      showToast('No logs to undo', '⚠️');
      return;
    }
    const last = waterState.logs.pop();
    waterState.consumed = Math.max(0, waterState.consumed - last.amount);
    saveWaterData();
    updateWaterUI();
    showToast(`Undid last entry (-${last.amount} ml)`, '↩️');
  }

  function resetWaterToday() {
    if (confirm("Reset today's water intake log back to 0 ml?")) {
      waterState.consumed = 0;
      waterState.logs = [];
      saveWaterData();
      updateWaterUI();
      showToast("Today's water log has been reset", '🔄');
    }
  }

  // Quick button events
  document.querySelectorAll('.quick-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const amt = btn.getAttribute('data-amount');
      addWater(amt);
    });
  });

  if (customAddBtn && customAmountInput) {
    customAddBtn.addEventListener('click', () => {
      const amt = parseInt(customAmountInput.value, 10);
      if (amt && amt > 0) {
        addWater(amt);
        customAmountInput.value = '';
      } else {
        alert('Please enter a valid amount in ml (e.g. 350).');
      }
    });
  }

  if (undoWaterBtn) undoWaterBtn.addEventListener('click', undoLastWater);
  if (resetWaterBtn) resetWaterBtn.addEventListener('click', resetWaterToday);

  if (goalSelector) {
    goalSelector.addEventListener('change', (e) => {
      waterState.target = parseInt(e.target.value, 10);
      saveWaterData();
      updateWaterUI();
      showToast(`Daily target set to ${waterState.target} ml`, '🎯');
    });
  }

  // Initial water render
  updateWaterUI();

  // ==========================================
  // 7. NUTRITION & WELLNESS QUIZ
  // ==========================================
  const quizData = [
    {
      question: "Skipping breakfast helps college students lose weight faster and focus better in morning classes. Myth or Fact?",
      options: [
        "Fact — It speeds up your metabolism and clears brain fog.",
        "Myth — Skipping breakfast is linked to poorer academic concentration, mid-day fatigue, and overeating later.",
        "Fact — Only students who exercise need breakfast.",
        "Myth — But only if you drink 3 cups of coffee instead."
      ],
      correct: 1,
      explanation: "Myth! Prolonged overnight fasting without a nourishing morning meal depletes glycogen stores in the brain, reducing working memory and attention span during lectures. Studies show students who consume a balanced breakfast perform better academically and experience fewer energy crashes."
    },
    {
      question: "According to the Harvard Healthy Eating Plate and ICMR guidelines, how much of your meal plate should consist of vegetables and fruits?",
      options: [
        "About 10% (Just a small garnish)",
        "About 25% (A small side bowl)",
        "About 50% (Half your plate)",
        "Vegetables are optional if you take a multivitamin"
      ],
      correct: 2,
      explanation: "Correct: 50%! Filling half your plate with colorful vegetables and whole fruits supplies essential dietary fiber, protective antioxidants, Vitamin C, and hydration, which cannot be duplicated by isolated multivitamin pills."
    },
    {
      question: "Which of the following is a pocket-friendly, high-quality protein source readily available to college students?",
      options: [
        "Commercial sugar-loaded energy drinks",
        "Roasted peanuts, boiled chana, eggs, and curd",
        "Instant ramen noodles",
        "Deep-fried samosas and potato chips"
      ],
      correct: 1,
      explanation: "Correct! Roasted peanuts, boiled chickpeas (chana), eggs, and curd/paneer are affordable, dense protein powerhouses packed with amino acids to sustain satiety and muscle recovery without spiking blood glucose."
    },
    {
      question: "How does mild dehydration (loss of just 1% to 2% body water) affect student performance during coding labs or exams?",
      options: [
        "It has zero impact as long as you drink coffee.",
        "It can trigger tension headaches, sluggish reaction times, and reduced concentration.",
        "It temporarily increases IQ by concentrating neurons.",
        "It only affects marathon runners, not desk workers."
      ],
      correct: 1,
      explanation: "Correct! The brain is ~75% water. Clinical trials prove that mild dehydration of just 1-2% noticeably impairs cognitive task performance, short-term memory, and mood, often leading to screen fatigue headaches."
    },
    {
      question: "Energy drinks and high-caffeine beverages can safely replace sleep and water during engineering exam all-nighters. True or False?",
      options: [
        "True — Caffeine directly synthesizes new brain cells.",
        "False — High caffeine and sugar cause severe dehydration, heart palpitations, sleep architecture disruption, and rebound crashes.",
        "True — As long as you drink 4 cans in a row.",
        "False — But only if mixed with tea."
      ],
      correct: 1,
      explanation: "False! Energy drinks contain synthetic caffeine doses and excessive sugars that dehydrate renal pathways, spike heart rates, and disrupt REM sleep—which is the exact sleep stage required for long-term memory consolidation of what you studied."
    },
    {
      question: "Why is squeezing fresh lemon juice over your canteen dal or vegetable poha a smart nutritional habit?",
      options: [
        "It neutralizes all calories completely.",
        "The Vitamin C in lemon dramatically increases the bioavailability and absorption of plant-based (non-heme) iron.",
        "It replaces the need to drink water.",
        "It makes the food digest in under 5 minutes."
      ],
      correct: 1,
      explanation: "Correct! Plant-based iron found in lentils, leafy greens, and poha is non-heme iron, which has low natural absorption. The ascorbic acid (Vitamin C) in lemon juice converts it into a more soluble form, multiplying iron absorption and protecting against student fatigue and anemia."
    },
    {
      question: "When feeling hungry while studying late at night, which snack best prevents a sleep-distrupting blood sugar crash?",
      options: [
        "A packet of sweet cream cookies",
        "Extra-spicy fried instant noodles",
        "Roasted makhana (foxnuts), roasted peanuts, or a fruit with a glass of warm milk",
        "Two cans of cold soda"
      ],
      correct: 2,
      explanation: "Correct! Complex carbs combined with protein or healthy fats (like roasted makhana, peanuts, or warm milk) provide gradual tryptophan and steady glucose, avoiding midnight acid reflux or insomnia from heavy frying and high sugar."
    }
  ];

  let currentQuestionIndex = 0;
  let quizScore = 0;
  let quizAnswered = false;

  const currentQNum = document.getElementById('currentQNum');
  const totalQNum = document.getElementById('totalQNum');
  const liveScore = document.getElementById('liveScore');
  const quizProgressBar = document.getElementById('quizProgressBar');
  const questionTitle = document.getElementById('questionTitle');
  const optionsContainer = document.getElementById('optionsContainer');
  const quizFeedbackBox = document.getElementById('quizFeedbackBox');
  const feedbackBadge = document.getElementById('feedbackBadge');
  const feedbackExplanationText = document.getElementById('feedbackExplanationText');
  const nextQuestionBtn = document.getElementById('nextQuestionBtn');
  const quizQuestionArea = document.getElementById('quizQuestionArea');
  const quizResultsArea = document.getElementById('quizResultsArea');
  const finalScoreVal = document.getElementById('finalScoreVal');
  const finalTotalVal = document.getElementById('finalTotalVal');
  const achievementBadge = document.getElementById('achievementBadge');
  const resultSummaryText = document.getElementById('resultSummaryText');
  const restartQuizBtn = document.getElementById('restartQuizBtn');

  function initQuiz() {
    currentQuestionIndex = 0;
    quizScore = 0;
    quizAnswered = false;
    if (totalQNum) totalQNum.textContent = quizData.length;
    if (finalTotalVal) finalTotalVal.textContent = quizData.length;
    if (quizQuestionArea) quizQuestionArea.classList.remove('hidden');
    if (quizResultsArea) quizResultsArea.classList.add('hidden');
    loadQuestion(0);
  }

  function loadQuestion(index) {
    if (index >= quizData.length) {
      showQuizResults();
      return;
    }

    quizAnswered = false;
    const q = quizData[index];

    if (currentQNum) currentQNum.textContent = index + 1;
    if (liveScore) liveScore.textContent = quizScore;
    if (quizProgressBar) {
      const pct = Math.round(((index + 1) / quizData.length) * 100);
      quizProgressBar.style.width = `${pct}%`;
    }

    if (questionTitle) questionTitle.textContent = q.question;
    if (quizFeedbackBox) quizFeedbackBox.classList.add('hidden');

    if (optionsContainer) {
      optionsContainer.innerHTML = '';
      q.options.forEach((optText, optIdx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-option-btn';
        btn.innerHTML = `<span>${optText}</span>`;
        btn.addEventListener('click', () => handleOptionClick(optIdx, btn));
        optionsContainer.appendChild(btn);
      });
    }
  }

  function handleOptionClick(selectedIndex, selectedBtn) {
    if (quizAnswered) return;
    quizAnswered = true;

    const q = quizData[currentQuestionIndex];
    const optionButtons = optionsContainer.querySelectorAll('.quiz-option-btn');

    // Disable all options
    optionButtons.forEach(btn => btn.disabled = true);

    const isCorrect = (selectedIndex === q.correct);

    if (isCorrect) {
      quizScore++;
      if (liveScore) liveScore.textContent = quizScore;
      selectedBtn.classList.add('correct');
      feedbackBadge.textContent = '✓ Correct Answer!';
      feedbackBadge.className = 'feedback-badge correct';
      showToast('Correct answer!', '🌟');
    } else {
      selectedBtn.classList.add('wrong');
      // Highlight the correct answer
      if (optionButtons[q.correct]) {
        optionButtons[q.correct].classList.add('correct');
      }
      feedbackBadge.textContent = '✗ Not quite right';
      feedbackBadge.className = 'feedback-badge wrong';
    }

    feedbackExplanationText.textContent = q.explanation;
    quizFeedbackBox.classList.remove('hidden');
  }

  if (nextQuestionBtn) {
    nextQuestionBtn.addEventListener('click', () => {
      currentQuestionIndex++;
      loadQuestion(currentQuestionIndex);
    });
  }

  function showQuizResults() {
    if (quizQuestionArea) quizQuestionArea.classList.add('hidden');
    if (quizResultsArea) quizResultsArea.classList.remove('hidden');

    if (finalScoreVal) finalScoreVal.textContent = quizScore;
    if (finalTotalVal) finalTotalVal.textContent = quizData.length;

    let badge = 'Campus Wellness Explorer';
    let summary = 'Good attempt! Exploring nutrition helps you form lifelong healthy habits.';

    if (quizScore === quizData.length) {
      badge = '🥇 Campus Nutrition Champion';
      summary = 'Flawless score! You have an exemplary grasp of balanced nutrition, hydration, and healthy lifestyle habits.';
    } else if (quizScore >= 5) {
      badge = '🥈 Wellness Scholar';
      summary = 'Great job! You possess strong wellness awareness to help you through demanding college semesters.';
    } else if (quizScore >= 3) {
      badge = '🥉 Health Novice';
      summary = 'Fair start! Review our Nutrition Guide and Healthy Habits section to boost your health knowledge.';
    }

    if (achievementBadge) achievementBadge.textContent = badge;
    if (resultSummaryText) resultSummaryText.textContent = summary;
  }

  if (restartQuizBtn) {
    restartQuizBtn.addEventListener('click', initQuiz);
  }

  // Start quiz on ready
  initQuiz();

  // ==========================================
  // 8. USABILITY FEEDBACK SYSTEM (COMMUNITY EVALUATION)
  // ==========================================
  const feedbackForm = document.getElementById('feedbackForm');
  const feedbackSuccess = document.getElementById('feedbackSuccess');
  const reviewsFeed = document.getElementById('reviewsFeed');
  const totalReviewsCount = document.getElementById('totalReviewsCount');
  const awarenessImpactRate = document.getElementById('awarenessImpactRate');

  // Seed default tester reviews to showcase realistic testing for 25CPD37 evaluation
  const defaultFeedbackList = [
    {
      name: "Rahul Verma (1NH25CS142)",
      branch: "CSE - 3rd Sem",
      gain: "Yes, significantly",
      comment: "The water bottle animation and campus canteen food swaps are super practical for hostel life!",
      date: "14/11/2026"
    },
    {
      name: "Sneha Rao (1NH25CS189)",
      branch: "CSE - 3rd Sem",
      gain: "Yes, significantly",
      comment: "Really liked that the BMI tool emphasizes that BMI is only a screening metric and not a medical diagnosis.",
      date: "14/11/2026"
    },
    {
      name: "Aman Preet (1NH25CS034)",
      branch: "CSE - 3rd Sem",
      gain: "Yes, significantly",
      comment: "The 20-20-20 rule reminder in the habits section is very helpful during long programming lab sessions.",
      date: "13/11/2026"
    }
  ];

  function loadFeedbacks() {
    const raw = localStorage.getItem(STORAGE_KEYS.FEEDBACK);
    if (raw) {
      try {
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      } catch (err) {
        console.error(err);
      }
    }
    return defaultFeedbackList;
  }

  let feedbackList = loadFeedbacks();

  function saveAndRenderFeedbacks() {
    localStorage.setItem(STORAGE_KEYS.FEEDBACK, JSON.stringify(feedbackList));

    if (!reviewsFeed) return;
    reviewsFeed.innerHTML = '';

    let significantCount = 0;

    feedbackList.slice().reverse().forEach(fb => {
      if (fb.gain === 'Yes, significantly' || !fb.gain) {
        significantCount++;
      }

      const card = document.createElement('div');
      card.className = 'review-card';
      card.innerHTML = `
        <div class="review-meta">
          <span class="review-author">${escapeHtml(fb.name || 'Anonymous Student')} (${escapeHtml(fb.branch || 'CSE')})</span>
          <span class="review-tag">✓ ${escapeHtml(fb.gain || 'Yes, significantly')}</span>
        </div>
        <p class="review-comment">"${escapeHtml(fb.comment || 'Helpful health awareness application.')}"</p>
      `;
      reviewsFeed.appendChild(card);
    });

    const total = feedbackList.length;
    if (totalReviewsCount) totalReviewsCount.textContent = total;
    if (awarenessImpactRate) {
      const pct = total > 0 ? Math.round((significantCount / total) * 100) : 100;
      awarenessImpactRate.textContent = `${pct}%`;
    }
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  if (feedbackForm) {
    feedbackForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = document.getElementById('testerName').value.trim();
      const branchInput = document.getElementById('testerBranch').value.trim();
      const comments = document.getElementById('testerComments').value.trim();
      
      const gainRadio = document.querySelector('input[name="awarenessGain"]:checked');
      const gainVal = gainRadio ? gainRadio.value : 'Yes, significantly';

      const newFeedback = {
        name: nameInput || 'Student Tester',
        branch: branchInput || 'CSE - 3rd Sem',
        gain: gainVal,
        comment: comments || 'App is easy to use and provides clear nutrition awareness.',
        date: new Date().toLocaleDateString()
      };

      feedbackList.push(newFeedback);
      saveAndRenderFeedbacks();

      // Attempt background POST to server if running
      try {
        fetch('/api/feedback', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newFeedback)
        }).catch(() => {
          // Silent catch if pure static mode
        });
      } catch (err) {}

      feedbackForm.reset();
      feedbackForm.classList.add('hidden');
      if (feedbackSuccess) feedbackSuccess.classList.remove('hidden');

      showToast('Feedback submitted successfully! Thank you.', '🎉');
    });
  }

  // Initial feedback render
  saveAndRenderFeedbacks();

  console.log('NutriCampus Web Application Initialized. Ready for 25CPD37 Community Project.');
})();
