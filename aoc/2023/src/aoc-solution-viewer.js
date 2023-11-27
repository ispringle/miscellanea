import { LitElement, css, html } from 'lit';

import { defaultStyles } from './style';
import './components/select-grid/select-grid.js';
import './components/day-card/day-card.js';

import Solutions from './day/';

/**
 * An example element.
 *
 * @slot - This element has a slot
 * @csspart button - The button
 */
export class AocSolutionViewer extends LitElement {
  static get properties() {
    return {
      year: { type: String },
    };
  }

  constructor() {
    super();
    this.year = '';
  }

  static get styles() {
    return [
      defaultStyles,
      css`
        :host {
          margin: 0 auto;
        }
        article {
          display: flex;
          flex-direction: column;
          align-items: center;
        }
      `,
    ];
  }

  render() {
    return html`
      <article>
        <header>
          <h2>Advent of Code ${this.year}</h2>
        </header>
        <select-grid>
          ${Object.entries(Solutions).map(
            ([day, func]) => html`
              <day-card day=${day} .solution=${func}></day-card>
            `,
          )}
        </select-grid>
      </article>
    `;
  }
}

window.customElements.define('aoc-solution-viewer', AocSolutionViewer);
