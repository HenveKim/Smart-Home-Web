document.addEventListener('DOMContentLoaded', function() {
    const showFormButtons = document.querySelectorAll('.showFormButton');
    const furnitureForms = document.querySelectorAll('.furniture-form');

    showFormButtons.forEach((button) => {
        button.addEventListener('click', function() {
            const room = this.getAttribute('data-room');
            const correspondingForm = document.getElementById(room);

            // 显示或隐藏相应房间的表单
            furnitureForms.forEach((form) => {
                if (form === correspondingForm) {
                    if (form.style.display === 'none' || form.style.display === '') {
                        form.style.display = 'block';
                    } else {
                        form.style.display = 'none';
                    }
                } else {
                    form.style.display = 'none'; // 隐藏其他表单
                }
            });
        });
    });
});
