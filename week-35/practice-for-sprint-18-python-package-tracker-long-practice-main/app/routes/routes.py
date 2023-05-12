from flask import Blueprint, render_template, redirect, url_for
from ..models.shipping_form import ShippingForm
from ..models.models import db, Package

bp = Blueprint("home", __name__, url_prefix="")

shipping_request = Blueprint("new_package", __name__, url_prefix="")

@bp.route("/")
def root_endpoint():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@shipping_request.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
    #   print('FORM DATA -->', form.data)
    #   FORM DATA --> {'sender_name': 'cxczc', 'recipient_name': 'zxczc', 'origin': 'Seattle', 'destination': 'Seattle', 'express_shipping': False, 'csrf_token': 'IjkzZjg4NzM2NTdlMGZlZTY4NjIyNzBhNzBiMzczY2Q4ZWQxMTM2MTMi.ZFw4MA.dL0lu-d9Y-8fMm0Hhny5RcFI0hw'}
        data = form.data
        new_package = Package(sender=data["sender_name"],
                            recipient=data["recipient_name"],
                            origin=data["origin"],
                            destination=data["destination"],
                            location=data["origin"])


        db.session.add(new_package)
        db.session.commit()
        return redirect('/')

    return render_template('shipping_request.html', form=form)
