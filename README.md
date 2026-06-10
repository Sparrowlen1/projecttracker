<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 120" width="100%" height="100%">
  <defs>
    <clipPath id="typing">
      <rect x="20" y="30" width="0" height="40">
        <animate attributeName="width" from="0" to="480" dur="3s" begin="0.5s" fill="freeze" />
      </rect>
    </clipPath>
    <style>
      .cursor {
        animation: blink 1s step-end infinite;
      }
      @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
      }
    </style>
  </defs>

  <!-- terminal bg -->
  <rect width="650" height="120" rx="8" fill="#0f0f17" stroke="#2a2a3a" stroke-width="1.5" />

  <!-- top bar -->
  <rect width="650" height="28" rx="8" fill="#181824" />
  <rect y="14" width="650" height="14" fill="#181824" />
  <circle cx="18" cy="14" r="5" fill="#ff5f56" />
  <circle cx="34" cy="14" r="5" fill="#ffbd2e" />
  <circle cx="50" cy="14" r="5" fill="#27c93f" />

  <!-- prompt -->
  <text x="15" y="68" fill="#5cd9a5" font-family="'Courier New', monospace" font-size="18" font-weight="bold">$</text>

  <!-- typed message -->
  <g clip-path="url(#typing)">
    <text x="38" y="68" fill="#e2e2e8" font-family="'Courier New', monospace" font-size="18">Welcome to my project!</text>
  </g>

  <!-- blinking cursor -->
  <text x="38" y="68" fill="#e2e2e8" font-family="'Courier New', monospace" font-size="18" class="cursor">
    <animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite" begin="3.5s" />
    █
  </text>
</svg>