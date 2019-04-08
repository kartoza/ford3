
const getSaqaQualificationsListElement = () => {
  return document.getElementById('saqa-qualifications-list')
}

const getAddQualificationButtonElement = () => {
  return document.querySelector('button[data-action="add-qualif"]')
}

const getRemoveQualificationButtonElement = () => {
  return document.querySelector('button[data-action="remove-qualif"]')
}

const getClearQualificationsButtonElement = () => {
  return document.querySelector('button[data-action="clear-qualifs"]')
}

const getCampusQualificationsListElement = () => {
  return document.getElementById('campus-qualifications-list')
}

const getSelectedQualificationsFromList = (list) => {
  return list.querySelectorAll('li.selected')
}

const getSaqaQualificationsInputElem = () => {
  return document.getElementById('id_campus-qualifications-saqa_ids')
}

const addSaqaQualification = (saqaId) => {
  let saqaIds = getSaqaQualificationsInputElem().value.split(' ')
  saqaIds.push(saqaId)
  getSaqaQualificationsInputElem().value = saqaIds.join(' ')
}

const removeSaqaQualification = (saqaId) => {
  let saqaIds = getSaqaQualificationsInputElem().value.split(' ')

  saqaIds = saqaIds.filter(function (value, index, arr) {
    return value !== saqaId
  })

  getSaqaQualificationsInputElem().value = saqaIds.join(' ')
}

const setToggleEvent = (elem) => {
  elem.addEventListener('click', function (evt) {
    if (evt.target.tagName !== 'A') { evt.target.classList.toggle('selected') }
  })
}

const setClickEventToLi = () => {
  const qualifElems = document.querySelectorAll('li[data-saqa-id]')
  qualifElems.forEach(function (qualifElem) {
    setToggleEvent(qualifElem)
  })
}

const setClickEventToAddButton = () => {
  const addQualifButton = getAddQualificationButtonElement()
  addQualifButton.addEventListener('click', function (evt) {
    evt.stopPropagation()

    const saqaQualifListElem = getSaqaQualificationsListElement()
    const selectedQualifElems = getSelectedQualificationsFromList(saqaQualifListElem)

    selectedQualifElems.forEach(function (selectedQualifElem) {
      // remove the selected class attached to the node
      selectedQualifElem.classList.remove('selected')

      // clone the node
      var clonedNode = selectedQualifElem.cloneNode(true)

      // hide the node
      selectedQualifElem.style.display = 'none'

      // append the cloned node to the campus qualifications list
      const campusQualifListElem = getCampusQualificationsListElement()
      campusQualifListElem.appendChild(clonedNode)

      setToggleEvent(clonedNode)

      let saqaId = selectedQualifElem.dataset['saqaId']
      addSaqaQualification(saqaId)
    })
  })
}

const setClickEventToRemoveButton = () => {
  var removeQualifButton = getRemoveQualificationButtonElement()
  removeQualifButton.addEventListener('click', function (evt) {
    evt.stopPropagation()
    const saqaQualifListElem = getSaqaQualificationsListElement()
    const campusQualifListElem = getCampusQualificationsListElement()
    var selectedQualifElems = getSelectedQualificationsFromList(campusQualifListElem)

    selectedQualifElems.forEach(function (selectedQualifElem) {
      var qualifElem = saqaQualifListElem.querySelector('li[data-saqa-id="' + selectedQualifElem.dataset['saqa-id'] + '"]')
      if (qualifElem) { qualifElem.style.display = 'list-item' }

      campusQualifListElem.removeChild(selectedQualifElem)

      let saqaId = selectedQualifElem.dataset['saqaId']
      removeSaqaQualification(saqaId)
    })
  })
}

const setClickEventToClearButton = () => {
  const button = getClearQualificationsButtonElement()
  const input = getSearchQualifInputElem()

  button.addEventListener('click', function (evt) {
    evt.stopPropagation()

    input.value = ''

    const saqaQualifListElem = getSaqaQualificationsListElement()
    saqaQualifListElem.querySelectorAll('li').forEach(function (li) {
      saqaQualifListElem.removeChild(li)
    })
  })
}
const getSearchQualifInputElem = () => {
  return document.querySelector('input[data-action="search-qualif"]')
}

const buildSaqaQualificationLiContent = (saqa) => {
  let linkText = document.createTextNode('(' + saqa.saqa_id + ')')
  let link = document.createElement('a')
  link.href = 'http://regqs.saqa.org.za/viewQualification.php?id=' + saqa.saqa_id
  link.target = '_blank'
  link.appendChild(linkText)
  return link
}

const displaySaqaQualificationsResults = (results) => {
  const list = getSaqaQualificationsListElement()
  list.querySelectorAll('li').forEach(function (li) {
    list.removeChild(li)
  })

  results.forEach(function (saqa) {
    let saqaNode = document.createElement('li')
    saqaNode.setAttribute('data-saqa-id', saqa.saqa_id)
    const saqaNodeContent = document.createTextNode(saqa.name)
    const saqaLink = buildSaqaQualificationLiContent(saqa)
    saqaNode.appendChild(saqaLink)
    saqaNode.appendChild(document.createTextNode('\u00A0'))
    saqaNode.appendChild(saqaNodeContent)

    list.appendChild(saqaNode)

    setToggleEvent(saqaNode)
  })
}

const ajaxSearchQualifications = (query) => {
  const url = '/ford3/saqa_qualifications?q=' + query
  const request = new XMLHttpRequest()
  request.open('GET', url, true)

  request.onload = function () {
    if (request.status >= 200 && request.status < 400) {
    // Success!
      var data = JSON.parse(request.responseText)
      displaySaqaQualificationsResults(data['results'])
    } else {
    // We reached our target server, but it returned an error

    }
  }

  request.onerror = function () {
  // There was a connection error of some sort
  }

  request.send()
}

const setSearchEvent = () => {
  let timeout = null
  const elem = getSearchQualifInputElem()
  elem.onkeyup = function (e) {
    clearTimeout(timeout)

    timeout = setTimeout(function () {
      if (elem.value.length > 3) { ajaxSearchQualifications(elem.value) }
    }, 842)
  }
}

const setupEvents = () => {
  setClickEventToLi()
  setClickEventToAddButton()
  setClickEventToRemoveButton()
  setClickEventToClearButton()
  setSearchEvent()
}

(function () {
  setupEvents()
})()




$('#add-qualification-event').click(function () {
        addQualificationEvent();
    }
);


 function addQualificationEvent(){
        let name_div = document.getElementById('div_id_4-name');
        let start_date_div = document.getElementById('div_id_4-date_start');
        let end_date_div = document.getElementById('div_id_4-date_end');
        let http_link_div = document.getElementById('div_id_4-http_link');

        let new_name_div = name_div.cloneNode(true);
        let new_start_date_div = start_date_div.cloneNode(true);
        let new_end_date_div = end_date_div.cloneNode(true);
        let new_http_link_div = http_link_div.cloneNode(true);
        clearElement(new_name_div);
        clearElement(new_start_date_div);
        clearElement(new_end_date_div);
        clearElement(new_http_link_div);

         // let new_hr = document.createElement('hr');
        let new_remove_button_row = document.createElement('div');
        new_remove_button_row.innerHTML = getRemoveGroupRow();
        let form_group = (
            document.getElementsByClassName('form-group')[0]);
        new_remove_button_row.classlist += 'row';

         // form_group.appendChild(new_hr);
        form_group.appendChild(new_remove_button_row)
        form_group.appendChild(new_name_div);
        form_group.appendChild(new_start_date_div);
        form_group.appendChild(new_end_date_div);
        form_group.appendChild(new_http_link_div);
        innitiateRemoveQualificationEventButtons();
}

 function clearElement(elementToClear) {
       $(elementToClear).find('input:text').val('');
};

 function innitiateRemoveQualificationEventButtons() {
    $('.remove-qualification-event-button').click(function() {

         for (let i = 0; i < 4; i++) {
                var parent_div = this.parentElement.parentElement.parentElement;
                parent_div.nextElementSibling.remove();
        };
        parent_div.remove();
    })
 }

 function getRemoveGroupRow() {
        let button_html = '<div class="remove-qualification-event-button">' +
            '<div class="remove-qualification-button-inner ">X</div></div>'
        let result = (  '<div class="row">' +
                        '<div class="col-11"><hr/></div><div class="col-1">' +
            button_html + '</div>')
        return result
}
