from IPython.display import display, HTML

def feedback_button() -> None:
    button = '''
    <style>
    .button {
        border: 0;
        padding: 16px 32px 16px 32px;
        text-align: center;
        font-size: 18px;
        display: flex;
        transition: color 5s, 
                    background 5s, 
                    box-shadow 1s ease-out;
        cursor: pointer;
        color: #003262;
        border-radius: 30px;
        margin: 10% auto;
        background: linear-gradient(145deg, #e2e2e2, #bebebe);
        box-shadow: 20px 20px 40px 10px #afafaf, 
                    -20px -20px 40px 10px #f7f7f7, 
                    inset 0 0 0px, 
                    inset 0 0 0px;
    }
    
    .button:hover {
        color: #D3D3D3;
        background: #003262;
        box-shadow: 0 0 0px #000000, 
                    0 0 0px #000000, 
                    inset 20px 20px 40px 10px #002a51, 
                    inset -20px -20px 40px 10px #003b73;
    }
    </style>

    <a href="https://docs.google.com/forms/d/e/1FAIpQLScDK227bq_qLJDLsysk-UOEXy7G6_7YuYHGp2ogzeRBh4OvEw/viewform">
        <button class="button">
            Fill out the feedback form here
        </button>
    </a>
    '''
    display(HTML(button))


