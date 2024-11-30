document.addEventListener('DOMContentLoaded', () => {
    // Добавьте функционал для подтверждения удаления задачи
    const deleteLinks = document.querySelectorAll('a[data-confirm]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            if (!confirm('Вы уверены, что хотите удалить эту задачу?')) {
                event.preventDefault();
            }
        });
    });
});
