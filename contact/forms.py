from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="your f**king email address")
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.split()) < 4:
            raise forms.ValidationError("Fewer than 4 words, you're too lazy!")
        return message
