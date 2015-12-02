frappe.ui.form.on("loan_registration", {
	onload: function(frm) {
	},
	refresh: function(frm) {
	var me = this
	if(!frm.doc.__islocal) {
			// cur_frm.add_custom_button(__('Make Ferro Order'), function() {
				cur_frm.cscript.make_ferro_order(); });
		}
	}

});
cur_frm.cscript.get_amount =function(){
	frappe.model.open_mapped_doc({
		method: "tbc.tbc.doctype.loan_registration.loan_registration.get_amount       ",
		frm: cur_frm
	});

}