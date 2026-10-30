# Client Scripts (`js`)

## Overview
Provides client-side interactivity for the portfolio website, including the header typewriter animation and multi-language navigation state management.

## Interface
- `runTypingEffect()`: Queries `#typing-text` DOM element and initiates typewriter effect with a 100ms delay.
- `typeText(text: string, typingElement: HTMLElement, delay: number)`: Incremental typewriter routine scheduling character insertion via `setTimeout`.
- `updateActiveLang()`: Evaluates `window.location.pathname` and toggles `.active` class across `.language-switch a` elements.
- Event Listener: Binds `DOMContentLoaded` to `runTypingEffect`.

## Invariants
- The `#typing-text` DOM element must exist on pages executing `runTypingEffect`.
- Language switch anchors (`.language-switch a`) must maintain consistent `href` matching supported prefixes (`/`, `/en`, `/es`).

## Side Effects
- DOM mutation: Sequentially modifies `textContent` of `#typing-text`.
- DOM mutation: Modifies `classList` on `.language-switch a` anchor elements.
- Timers: Spawns delayed execution timers via `setTimeout`.

## Verification
Run: `npm start`
