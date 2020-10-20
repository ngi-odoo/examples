# What
This module contains informations about `position` attribute.

This attribute is used to put a node in a specific place.

`position` attribute can be:
- before
- after
- inside
- replace
- move
- attributes

## before
The content you want to add is added before the target node

## after
The content you want to add is added inside the target node

## inside
This is the default position.

The content you want to add is appened inside the target node.

In the example (`views/res_partner.xml`), we put field `name_inside` inside page `sales_purchase`

## replace
The target node is replaced by the content you want to add

## move
Move the target content to another place

## attributes
Using `position="attributes"` is a bit special.

`attributes` is used to add, edit or delete existing or non-existing attributes.

With that, you can add attributes like `invisible="..."` for a specific field, group or page.

# Examples
Examples for `before`, `after`, `inside`, `replace` are in `views/res_partner.xml` files.

# Warning
## Incorrect display
As you can see with field `incorrect_display`, `incorrect_display2`, `incorrect_display3` and `incorrect_display4`, some fields could not be correctly displayed.

### incorrect_display and incorrect_display2
Labels for these two fields are not present so these two fields are not correctly placed.

Switch to `edit` mode to see where these fields are.

This probably occures because `replace` as been used and replaces the original field (here `street` and `mobile`) (see [mobile field declaration](https://github.com/odoo/odoo/blob/c61db20204700a375f7005f50f95b44a60c3bb70/odoo/addons/base/views/res_partner_views.xml#L266) and [mobile field replace](https://github.com/odoo/odoo/blob/c61db20204700a375f7005f50f95b44a60c3bb70/addons/sms/views/res_partner_views.xml#L20))

In fact, when we want to add `incorrect_display2` after `mobile`, it's placed at the correct place (after `mobile`, so inside the `<div class="o_row">` that is after the `<label>` declaration).

This is why it's not at the place we want it to be (and (I think) why the corresponding label is not created)

# More
[More information here](https://www.odoo.com/documentation/13.0/reference/views.html#inheritance-specs)
