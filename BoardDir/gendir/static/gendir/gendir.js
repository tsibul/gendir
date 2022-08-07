function colapse(id){
    var area = 'collapse_' + id;
    var button = area + '_but';
    var button_minus = '<button type=button class="btn btn-sm btn-outline-secondary" ><i class="fas fa-minus"></i></button>';
    var button_plus = '<button type=button class="btn btn-sm btn-outline-primary" ><i class="fas fa-plus"></i></button>';
    if (document.getElementById(area).style.display =='none'){
    document.getElementById(button).innerHTML = button_minus;
    document.getElementById(area).style.display = 'inline';}
    else {document.getElementById(button).innerHTML = button_plus;
    document.getElementById(area).style.display = 'none';};

}