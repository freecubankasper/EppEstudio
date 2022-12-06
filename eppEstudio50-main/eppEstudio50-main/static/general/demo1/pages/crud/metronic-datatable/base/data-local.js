'use strict';

var KTDatatableDataLocalDemo = function() {

	var demo = function() {

		var datatable = $('.kt-datatable').KTDatatable({
			layout: {
				scroll: false, // enable/disable datatable scroll both horizontal and vertical when needed.
				// height: 450, // datatable's body's fixed height
				footer: false // display/hide footer
			},

			sortable: false,

			pagination: false
		});
	};

	return {
		init: function() {
			demo();
		}
	};
}();

jQuery(document).ready(function() {
	KTDatatableDataLocalDemo.init();
});