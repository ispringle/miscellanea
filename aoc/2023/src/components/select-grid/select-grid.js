import { LitElement, css, html } from 'lit'
import { repeat } from 'lit/directives/repeat.js'

import { defaultStyles } from '../../style'

export class SelectGrid extends LitElement {
  static get properties () {
    return {
      expandedCard: { type: String }
    }
  }

  static get styles () {
    return [
      defaultStyles,
      css`
        :host {
          width: 100%;
          margin: 5px;
        }
        .grid {
          display: grid;
          grid-template-columns: repeat(2, auto);
          gap: 10px;
        }
        .open-close-icon {
          float: right;
          margin: 5px;
        }
      `
    ]
  }
  constructor () {
    super()
    this.day = 'One'
    this.input = ''
    this.expandedCard
  }

  onClick(event) {
    // this.expandedCard = event.target.dataset.card
  }

  renderCard (el) {
    const id = `grid-card-${el.day}`
    const expandIcon = 'fullscreen'
    const closeIcon = 'close_fullscreen'
    const focused = this.expandedCard === id
    const icon = focused ? closeIcon : expandIcon
    const focusClass = focused ? "hidden" : ""
    return html`
      <div .class=${`card ${focusClass}`} id=${id}>
        <span
          @click=${this.onClick}
          class="material-symbols-outlined open-close-icon"
          data-card=${id}
          >${icon}</span
        >
        ${el}
      </div>
    `
  }

  render () {
    console.log(this.children)
    return html`
      <div class="grid">
        ${repeat(this.children, child => child.day, this.renderCard.bind(this))}
      </div>
    `
  }
}

window.customElements.define('select-grid', SelectGrid)
