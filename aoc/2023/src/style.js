import { css } from 'lit';

export const defaultStyles = css`
  /*! concrete.css v2.0.3 | MIT License | github.com/louismerlin/concrete.css */

  /**
 * 1. Modify the base font-size to 62.5% so that 1.6rem = 16px.
 * 2. Set box-sizing globally to handle padding and border widths.
 */

  html {
    font-size: 62.5%; /* 1 */
    box-sizing: border-box; /* 2 */
  }

  /**
 * 1. Continue the global box-sizing modification.
 * 2. Set the underline size for all elements.
 */

  *,
  ::after,
  ::before {
    box-sizing: inherit; /* 1 */
    text-decoration-thickness: 0.2rem; /* 2 */
  }

  /**
 * 1. Set global font size to 2rem (20px) with a normal weight.
 * 2. Set the text and background color to white and black by default.
 * 3. Set the font-family to Helvetica, or equivalent.
 */

  body {
    font-size: 2rem; /* 1 */
    font-weight: 400; /* 1 */
    background: #fff; /* 2 */
    color: #111; /* 2 */
    font-family: Helvetica, Arial, sans-serif; /* 3 */
  }

  /**
 * Set the link color to black
 */

  a {
    color: #111;
  }

  /**
 * 1. Set the max width of images to 100%, so that they don't overflow.
 * 2. Set the height of images relative to their width.
 */

  img {
    max-width: 100%; /* 1 */
    height: auto; /* 2 */
  }

  /** 
 * 1. Center the main element horizontally.
 * 2. Set the width of the element to 640px, with padding for mobile screens.
 */

  main {
    margin: auto; /* 1 */
    max-width: 66rem; /* 2 */
    padding: 0 1rem; /* 2 */
    width: 100%; /* 2 */
  }

  /**
 * 1. Add some padding around the header.
 * 2. Increase the size of text in the header.
 */

  header {
    padding: 16rem 0; /* 1 */
    font-size: 1.2em; /* 2 */
  }

  /**
 * Center the text in the footer.
 */

  footer {
    text-align: center;
  }

  /**
 * Add some padding around the sections.
 */

  section {
    padding: 4rem 0;
  }

  /**
 * 1. Change the style of the button.
 * 2. Set the color and border of the button.
 * 3. Add the pointer cursor when hovering a button.
 */

  button,
  input[type='button'],
  input[type='reset'],
  input[type='submit'] {
    display: inline-block; /* 1 */
    vertical-align: middle; /* 1 */
    padding: 0.4rem 1rem; /* 1 */
    font-size: 2rem; /* 1 */
    font-weight: normal; /* 1 */
    margin-bottom: 1rem; /* 1 */
    background: #fff; /* 2 */
    color: #111; /* 2 */
    border: 0.2rem solid #111; /* 2 */
    border-radius: 0; /* 2 */
    cursor: pointer; /* 3 */
  }

  /**
 * 1. Invert the colors of the disabled button.
 * 2. Add the not-allowed cursor when hovering a disabled button.
 */

  button:disabled,
  input[type='button']:disabled,
  input[type='reset']:disabled,
  input[type='submit']:disabled {
    color: #fff; /* 1 */
    background: #111; /* 1 */
    cursor: not-allowed; /* 2 */
  }

  /**
 * Set the list bullet to square.
 */

  ul {
    list-style: square;
  }

  /**
 * Set the border around a fieldset.
 */

  fieldset {
    border: 0.2rem solid #111;
  }

  /**
 * 1. Modify the display of labels and legends.
 * 2. Add a margin underneath.
 */

  label,
  legend {
    display: block; /* 1 */
    font-weight: bold; /* 1 */
    margin-bottom: 0.8rem; /* 2 */
  }

  /** 
 * 1. Change the appearance of the text input.
 * 2. Set the color and border of the text input.
 */

  input[type='email'],
  input[type='number'],
  input[type='password'],
  input[type='search'],
  input[type='tel'],
  input[type='text'],
  input[type='url'],
  textarea,
  select {
    -webkit-appearance: none; /* 1 */
    -moz-appearance: none; /* 1 */
    appearance: none; /* 1 */
    box-shadow: none; /* 1 */
    box-sizing: inherit; /* 1 */
    padding: 0.4rem 1rem; /* 1 */
    width: 100%; /* 1 */
    font-size: 2rem; /* 1 */
    color: #111; /* 2 */
    background-color: #fff; /* 2 */
    border: 0.2rem solid #111; /* 2 */
    border-radius: 0; /* 2 */
  }

  /**
 * Set margin for form elements.
 */

  fieldset,
  input,
  select,
  textarea {
    margin: 0 0 1.6rem 0;
  }

  /**
 * 1. Set the font color for the placeholder in inputs.
 * 2. Set font-style to italic for the placeholder in inputs.
 */

  input::placeholder,
  textarea::placeholder {
    color: #111; /* 1 */
    font-style: italic; /* 2 */
  }

  /**
 * 1. Expand width to 100% for the table element.
 * 2. Remove the distance between the borders of adjacent table cells.
 */

  table {
    width: 100%; /* 1 */
    border-spacing: 0; /* 2 */
  }

  /**
 * Add padding around table cells.
 */

  td,
  th {
    padding: 0.8rem;
  }

  /**
 * Remove left padding for first cell in a row.
 */

  td:first-child,
  th:first-child {
    padding-left: 0;
  }

  /**
 * Remove right padding for last cell in a row.
 */

  td:last-child,
  th:last-child {
    padding-right: 0;
  }

  /**
 * 1. Add a border under the table header.
 * 2. Align the text to the left in the table header.
 */

  th {
    border-bottom: 0.2rem solid #111; /* 1 */
    text-align: left; /* 2 */
  }

  /**
 * Add a thiner border under table rows.
 */

  td {
    border-bottom: 0.1rem solid #111;
  }

  /**
 * 1. Change the margins and padding.
 * 2. Add a border on the left of these elements.
 * 3. Set the y overflow to hidden to hide the navigation bar.
 */

  blockquote,
  pre {
    margin-left: 0; /* 1 */
    margin-right: 0; /* 1 */
    padding: 1rem 1.6rem; /* 1 */
    border-left: 0.2rem solid #111; /* 2 */
    overflow-y: hidden; /* 3 */
  }

  /**
 * 1. Set the rest of the border of the preformatted element to dotted.
 * 2. Re-set the left border style.
 */

  pre {
    border: 0.1rem dotted #111;
    border-left: 0.2rem solid #111;
  }

  /**
 * 1. Modify the display of the code block.
 * 2. Reduce the font size of the code block.
 */

  pre > code {
    white-space: pre; /* 1 */
    display: block; /* 1 */
    font-size: 1.6rem; /* 2 */
  }

  /**
 * 1. Modify the display of the progress bar in all browsers.
 * 2. Set the colors and border of the progress bar.
 */

  progress {
    -moz-appearance: none; /* 1 */
    -webkit-appearance: none; /* 1 */
    display: block; /* 1 */
    height: 1rem; /* 1 */
    overflow: hidden; /* 1 */
    padding: 0; /* 1 */
    width: 100%; /* 1 */
    background: #fff; /* 2 */
    color: #111; /* 2 */
    border: 0.2rem solid #111; /* 2 */
    border-radius: 0; /* 2 */
  }

  /**
 * Set the background color of the webkit progress bar.
 */

  progress::-webkit-progress-bar {
    background-color: #fff;
  }

  /**
 * Set the color of the webkit progress bar.
 */

  progress::-webkit-progress-value {
    background-color: #111;
  }

  /**
 * Set the color of the mozilla progress bar.
 */

  progress::-moz-progress-bar {
    background-color: #111;
  }

  /**
 * Set the border for the horizontal rule.
 */

  hr {
    border: 0.1rem solid #111;
  }

  /**
 * Invert the colors if the user has dark mode activated.
 */

  @media (prefers-color-scheme: dark) {
    body {
      background: #111;
      color: #fff;
    }
    a,
    input::placeholder,
    textarea::placeholder {
      color: #fff;
    }
    button,
    input[type='button'],
    input[type='reset'],
    input[type='submit'],
    input[type='email'],
    input[type='number'],
    input[type='password'],
    input[type='search'],
    input[type='tel'],
    input[type='text'],
    input[type='url'],
    textarea,
    select,
    progress {
      background: #111;
      color: #fff;
      border-color: #fff;
    }
    button:disabled,
    input[type='button']:disabled,
    input[type='reset']:disabled,
    input[type='submit']:disabled {
      color: #111;
      background: #fff;
    }
    fieldset {
      border-color: #fff;
    }
    td,
    th,
    blockquote,
    pre,
    hr {
      border-color: #fff;
    }
    progress::-webkit-progress-bar {
      background-color: #111;
    }
    progress::-webkit-progress-value {
      background-color: #fff;
    }
    progress::-moz-progress-bar {
      background-color: #fff;
    }
  }

  /* fallback */
  @font-face {
    font-family: 'Material Symbols Outlined';
    font-style: normal;
    font-weight: 400;
    src: url(https://fonts.gstatic.com/s/materialsymbolsoutlined/v151/kJF1BvYX7BgnkSrUwT8OhrdQw4oELdPIeeII9v6oDMzByHX9rA6RzaxHMPdY43zj-jCxv3fzvRNU22ZXGJpEpjC_1v-p_4MrImHCIJIZrDCvHOelbd5zrDAt.woff)
      format('woff');
  }

  .material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    -moz-font-feature-settings: 'liga';
    -moz-osx-font-smoothing: grayscale;
  }
`;
