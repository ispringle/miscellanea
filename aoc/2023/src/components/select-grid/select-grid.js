import { LitElement, css, html } from 'lit';
import { repeat } from 'lit/directives/repeat.js';

import { defaultStyles } from '../../style';

export class SelectGrid extends LitElement {
  static get properties() {
    return {
      expandedCard: { type: String },
      cards: { type: Array },
    };
  }

  static get styles() {
    return [
      defaultStyles,
      css`
        :host {
          width: 100%;
          margin: 5px;
          display: grid;
          grid-template-columns: repeat(auto-fit, 50rem);
          grid-auto-flow: dense;
          grid-auto-rows: 1fr;
          gap: 10px;
        }
        .open-close-icon {
          float: right;
          margin: 5px;
        }
        .focused {
          grid-column: 1 / -1;
        }
        .hidden {
          display: none;
        }
      `,
    ];
  }
  constructor() {
    super();
    this.day = 'One';
    this.input = '';
    this.expandedCard = '';
    this.cards = [];
  }

  connectedCallback() {
    super.connectedCallback();
    const cards = [];
    Array.from(this.children).forEach((child) => {
      child.slot = child.day;
      cards.push(child.day);
    });
    this.cards = cards;
  }

  firstUpdated() {
    const mo = new MutationObserver(() => this.requestUpdate());
    mo.observe(this, { childList: true });
  }

  onClick(id) {
    this.expandedCard = this.expandedCard === id ? '' : id;
  }

  renderCard(id) {
    const focused = this.expandedCard === id;
    const icon = focused ? 'close_fullscreen' : 'fullscreen';
    const className = focused
      ? 'focused'
      : this.expandedCard === ''
        ? ''
        : 'hidden';
    return html`
      <div class=${className}>
        <span
          @click=${() => this.onClick(id)}
          class="material-symbols-outlined open-close-icon"
          >${icon}</span
        >
        <slot name=${id}></slot>
      </div>
    `;
  }

  render() {
    return html`
      ${repeat(this.cards, (card) => card, this.renderCard.bind(this))}
    `;
  }
}

window.customElements.define('select-grid', SelectGrid);
