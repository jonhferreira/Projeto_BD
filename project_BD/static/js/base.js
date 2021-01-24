const op_menu = document.querySelectorAll('.op_menu')
let musicas = []
let container = document.querySelector('.container')
let input = container.querySelector('input')
let playlist = document.querySelector('.playlist')

op_menu.forEach((item) => item.addEventListener('click', (e) => {
	e.preventDefault();
}))

input.addEventListener('keyup', AddMusic)

function AddMusic(event) {
	const KeyPressedIsEnter = event.key == 'Enter'
	if(KeyPressedIsEnter) {
		input.value.split(',').forEach( musica => {
			if(musica) {
				musicas.push(musica.trim())
			}
		})
		updateMusics()
		input.value=''
	}
}

function updateMusics() {
	clearMusic()

	musicas.slice().reverse().forEach( musica => {
		playlist.prepend(createMusic(musica))
	})
}

function createMusic(musica) {
	const div = document.createElement('div')
	div.classList.add('tag')

	const span = document.createElement('span')
	span.innerHTML = musica
	div.appendChild(span)
	
	const i = document.createElement('i')
	i.classList.add('close')
	i.setAttribute('data-id', musica)
	i.onclick = removeMusic
	div.append(i)

	return div
}

function removeMusic(event) {
	const buttonX = event.currentTarget
	const id = buttonX.dataset.id
	const index = musicas.indexOf(id)
	musicas.splice(index, 1)

	updateMusics()
}

function clearMusic() {
	playlist.querySelectorAll('.tag').forEach( tagElement => tagElement.remove() )
}
