const ctxShow = (event) => {
  if (event.button == 2) {
    event.preventDefault()
    const menu = document.getElementsByClassName('context-menu')[0]

    menu.classList.add('context-menu-active')
    menu.style.left = event.pageX + 'px'
    menu.style.top = event.pageY + 'px'
  }  
}

const ctxHide = (event) => {
  const ctxMenu = document.getElementsByClassName('context-menu')[0]
  ctxMenu.classList.remove('context-menu-active')
}

const ctxItemClick = (menuActions) => {
  const menu = document.getElementsByClassName('context-menu')[0]

  return (event) => {
    const id = event.target.getAttribute('id')

    if (Object.keys(menuActions).includes(id)) {
      menuActions[id]()
    }

    menu.classList.remove('context-menu-active')
  }
}

export {ctxShow, ctxHide, ctxItemClick}
