$(document).ready(function () {
    $('#data-table').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'csvHtml5',
                fieldBoundary: '',
                text: 'export',
                exportOptions: {
                    columns: [-1]
                }
            },
            {
                extend: 'copy',
                fieldBoundary: '',
                text: 'copy',
                exportOptions: {
                    columns: [-1]
                }
            },
            {
                text: 'All',
                action: function () {
                    location.reload(true);
                }
            },
            {
                text: 'Viruses',
                action: function () {
                    var table = $('#data-table').DataTable();
                    table.column(4).search('ccc').draw();
                }
            },
            {
                text: 'Archaea',
                action: function () {
                    var table = $('#data-table').DataTable();
                    table.column(4).search('ccc').draw();
                }
            }
        ],
        select: true
    });
});

