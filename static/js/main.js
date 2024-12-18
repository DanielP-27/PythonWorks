const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete) {
  const btnConfirm = Array.from(btnDelete);
  btnConfirm.forEach((btn) =>{
    btn.addEventListener('click', (e) => {
      if(!confirm('Please, confirm you would like to delete this data')){
        e.preventDefault();
      }
    });
  });
}