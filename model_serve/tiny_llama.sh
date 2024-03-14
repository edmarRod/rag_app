wget -nc https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
chmod +x TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --server --port 8080 --nobrowser -ngl 9999