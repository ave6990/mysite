import {ctxShow, ctxHide, ctxItemClick} from './contextMenu.js'

const unselectAll = () => {
  const rows = Array.from(document.getElementsByClassName('selected'))

  for (let r of rows) {
    r.classList.remove('selected')
  }
}

const selectAll = () => {
  const rows = document.querySelectorAll('tr')

  for (let r of rows) {
    if (r.querySelectorAll('td').length > 0) {
      r.classList.add('selected')
    }
  }
}

const selectEventHandler = (event) => {
  if (event.target.tagName == 'TD') {
    const tr = event.target.parentNode

    if (event.ctrlKey) {
      tr.classList.toggle('selected')
    }
    if (event.shiftKey) {
      const rows = Array.from(document.getElementsByClassName('selected'))
      const current = tr.id.split(':').pop()
      let from = current
      let to = current

      unselectAll()

      if (rows.length > 0) {
        from = rows[0].id.replace('selected', '').trim().split(':').pop()

        if (rows.length > 1) {
          to = rows.pop().id.replace('selected', '').trim().split(':').pop()
        } 
      }

      for (let i = Math.min(from, to, current); i <= Math.max(from, to, current); i++) {
          document.getElementById('row:' + i).classList.add('selected')
      }
    }
  }
}

const pass = () => {}

const ctxCommands = {
  'ctx-unselect-all': unselectAll,
  'ctx-select-all': selectAll,
  'ctx-save': pass,
  'ctx-copy': pass,
  'ctx-delete': pass
}

const addEventListeners = () => {
  const table = document.getElementsByTagName('tbody')
  const ctxMenu = document.getElementsByClassName('context-menu')[0]

  for (let el of table) {
    el.addEventListener('click', selectEventHandler)
    el.addEventListener('contextmenu', ctxShow)
  }

  ctxMenu.addEventListener('click', ctxItemClick(ctxCommands))

  document.body.addEventListener('click', ctxHide)
}

document.addEventListener("DOMContentLoaded", (event) => {
  addEventListeners()
})
