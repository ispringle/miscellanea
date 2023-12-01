import { LitElement, css, html } from 'lit';
import { defaultStyles } from '../../style';

export class DayCard extends LitElement {
  static get properties() {
    return {
      day: { type: String },
      solution: { attribute: false },
      partOneSolution: { type: String },
      partTwoSolution: { type: String },
    };
  }

  static get styles() {
    return [
      defaultStyles,
      css`
        section {
          border: solid 2px;
          padding: 10px;
        }
        section:hover {
          box-shadow: black 5px 5px;
        }
        h3 {
          text-transform: capitalize;
        }
        input[type='text'],
        textarea {
          width: 90%;
        }
      `,
    ];
  }

  constructor() {
    super();
    this.day = '';
    this.input = '';
    this.partOneSolution = '';
    this.partTwoSolution = '';
    this.solution = null;
  }

  onChange(event) {
    this.input = event.target.value.trim();
  }

  solve(event) {
    event.preventDefault();
    const [one, two] = this.solution.solve(this.input, this.input);
    this.partOneSolution = one;
    this.partTwoSolution = two;
  }

  test(event) {
    event.preventDefault();
    const {testInputOne, testInputTwo } = this.solution.testInputs;
    const [one, two] = this.solution.solve(testInputOne, testInputTwo);
    this.partOneSolution = one;
    this.partTwoSolution = two;
  }

  visualize(event) {
    event.preventDefault();
    this.solution.visualize();
  }

  render() {
    // this.input = this.solution.testInputs.testInputOne;

    return html`
      <section>
        <h3>Day ${this.day} Solution</h3>
        <form>
          <fieldset>
            <legend>Input</legend>
            <textarea
              placeholder="Paste your input here..."
              .value=${this.input}
              @change=${this.onChange}
            ></textarea>
            <input type="submit" value="Solve" @click=${this.solve} />
            <input type="submit" value="Test" @click=${this.test} />
          </fieldset>
        </form>
        <fieldset>
          <legend>Solution</legend>
          <label for=${`${this.day}-part-one`}>Part One</label>
          <input
            readonly
            id=${`${this.day}-part-one`}
            type="text"
            value=${this.partOneSolution}
          />
          <label for=${`${this.day}-part-two`}>Part Two</label>
          <input
            readonly
            id=${`${this.day}-part-two`}
            type="text"
            value=${this.partTwoSolution}
          />
          ${this.solution.visualize
            ? html`
                <input
                  type="submit"
                  value="Visualize"
                  @click=${this.visualize}
                />
              `
            : ''}
        </fieldset>
      </section>
    `;
  }
}

window.customElements.define('day-card', DayCard);
