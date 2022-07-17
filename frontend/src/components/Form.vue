<template>
    <div id="container">
        <h1 id="title">Word counter</h1>
        <form id="word-form" @submit="getNumberOfWords">
            <textarea :class="{'textarea-danger':error}" type="textarea" id="textarea" name="text" v-model="text" placeholder="Type some text" />
            <span id="error" v-show="error !== null">{{error}}</span>
            <input id="input-btn" type="submit" value="Submit" />
        </form>

        <h3 id="result" v-show="numberOfWords > 0">Number of words: {{numberOfWords}}</h3>
    </div>
        
</template>

<script>
export default {
    name: "Form",
    data() {
        return {
            text: null,
            error: null,
            numberOfWords: 0
        }
    },
    methods: {
        async getNumberOfWords(e) {
            e.preventDefault();
            if(this.text !== null && this.text !== ''){
                const data = {
                text: this.text
                }
                const dataJson = JSON.stringify(data);
                const request = await fetch("/api/v1/core/", {
                    method: "POST", 
                    headers: {"Content-Type": "application/json"}, 
                    body: dataJson
                });
                const response = await request.json();
                this.error = null;
                this.numberOfWords = response.text;
            } else {
                this.numberOfWords = 0
                this.error = "You need to type some text before submit."
            }
            
        }
    }
}
</script>

<style scoped>
    #container {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
    }
    #title {
        color: #302D68;
    }
    #word-form {
        max-width: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #title {
        margin-bottom: 10px;
    }
    #textarea {
        width: 400px;
        height: 200px;
        padding: 10px;
    }

    .textarea-danger {
        border: 1px solid #ff3333;
    }

    #input-btn {
        width: 200px;
        height: 30px;
        background-color: #03C5E1;
        color: white;
        border: none;
        border-radius: 20px;
        margin-top: 20px;
        transition: 0.5s;
    }
    #input-btn:hover {
        cursor: pointer;
        background-color: transparent;
        color: #03C5E1;
        border: 1px solid #03C5E1;
    }
    #result {
        margin-top: 10px;
        color: #302D68;
    }
    #error {
        margin-top: 10px;
        color: #ff3333;
        font-size: 14px;
    }
</style>