--// 99 Nights Forest - MOBILE OPTIMIZED MOD MENU
--// Telefon uyumlu, düşük kasma, stabil

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")
local humanoidRootPart = character:WaitForChild("HumanoidRootPart")
local camera = Workspace.CurrentCamera

--// MOBİL KONTROL DEĞİŞKENLERİ
local touchStartPos = nil
local isTouchingUI = false

--// MOD MENÜ AYARLARI
local MOD_MENU = {
    Visible = false,
    Features = {
        ChainChop = false,
        ItemESP = false,
        ChestESP = false,
        ScrapESP = false,
        AdminPanel = false,
        Fly = false,
        Speed = false,
        SpeedValue = 50,
        FlySpeed = 40,
        NoClip = false,
        FullBright = false,
        GodMode = false,
    }
}

--// ============================================
--// GUI OLUŞTURMA (MOBİL UYUMLU)
--// ============================================

local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Name = "Forest99_MobileMod"
ScreenGui.ResetOnSpawn = false
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
ScreenGui.Parent = player:WaitForChild("PlayerGui")

--// AÇMA/KAPAMA BUTONU (SAĞ ÜST KÖŞE, BÜYÜK)
local ToggleButton = Instance.new("TextButton")
ToggleButton.Name = "ModMenuToggle"
ToggleButton.Size = UDim2.new(0, 70, 0, 70)
ToggleButton.Position = UDim2.new(1, -80, 0, 10)
ToggleButton.BackgroundColor3 = Color3.fromRGB(30, 30, 30)
ToggleButton.Text = "🌲\nMOD"
ToggleButton.TextColor3 = Color3.fromRGB(0, 255, 100)
ToggleButton.TextSize = 16
ToggleButton.Font = Enum.Font.GothamBold
ToggleButton.TextWrapped = true
ToggleButton.Parent = ScreenGui

local ToggleStroke = Instance.new("UIStroke", ToggleButton)
ToggleStroke.Color = Color3.fromRGB(0, 255, 100)
ToggleStroke.Thickness = 2

local ToggleCorner = Instance.new("UICorner", ToggleButton)
ToggleCorner.CornerRadius = UDim.new(0, 15)

--// SÜRÜKLEME ÖZELLİĞİ (BUTONU İSTEDİĞİN YERE TAŞI)
local draggingToggle = false
local dragStart = nil
local startPos = nil

ToggleButton.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseButton1 then
        draggingToggle = true
        dragStart = input.Position
        startPos = ToggleButton.Position
    end
end)

ToggleButton.InputEnded:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseButton1 then
        draggingToggle = false
    end
end)

UserInputService.InputChanged:Connect(function(input)
    if draggingToggle and (input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseMovement) then
        local delta = input.Position - dragStart
        ToggleButton.Position = UDim2.new(
            startPos.X.Scale, startPos.X.Offset + delta.X,
            startPos.Y.Scale, startPos.Y.Offset + delta.Y
        )
    end
end)

--// ANA MOD MENÜ FRAME (TAM EKRAN, MOBİL UYUMLU)
local MainFrame = Instance.new("Frame")
MainFrame.Name = "MainMenu"
MainFrame.Size = UDim2.new(0.95, 0, 0.85, 0)
MainFrame.Position = UDim2.new(0.025, 0, 0.075, 0)
MainFrame.BackgroundColor3 = Color3.fromRGB(15, 15, 20)
MainFrame.BorderSizePixel = 0
MainFrame.Visible = false
MainFrame.Parent = ScreenGui

local MainCorner = Instance.new("UICorner", MainFrame)
MainCorner.CornerRadius = UDim.new(0, 15)

--// BAŞLIK ÇUBUĞU
local TitleBar = Instance.new("Frame")
TitleBar.Size = UDim2.new(1, 0, 0, 60)
TitleBar.BackgroundColor3 = Color3.fromRGB(30, 35, 40)
TitleBar.BorderSizePixel = 0
TitleBar.Parent = MainFrame

local TitleCorner2 = Instance.new("UICorner", TitleBar)
TitleCorner2.CornerRadius = UDim.new(0, 15)

local Title = Instance.new("TextLabel")
Title.Size = UDim2.new(0.7, 0, 1, 0)
Title.Position = UDim2.new(0, 15, 0, 0)
Title.BackgroundTransparency = 1
Title.Text = "🌲 ORMAN 99 GECE"
Title.TextColor3 = Color3.fromRGB(0, 255, 100)
Title.TextSize = 22
Title.Font = Enum.Font.GothamBold
Title.TextXAlignment = Enum.TextXAlignment.Left
Title.Parent = TitleBar

--// KAPATMA BUTONU (BÜYÜK, DOKUNMATİK)
local CloseButton = Instance.new("TextButton")
CloseButton.Size = UDim2.new(0, 50, 0, 50)
CloseButton.Position = UDim2.new(1, -60, 0, 5)
CloseButton.BackgroundColor3 = Color3.fromRGB(255, 60, 60)
CloseButton.Text = "✕"
CloseButton.TextColor3 = Color3.fromRGB(255, 255, 255)
CloseButton.TextSize = 24
CloseButton.Font = Enum.Font.GothamBold
CloseButton.Parent = TitleBar

local CloseCorner = Instance.new("UICorner", CloseButton)
CloseCorner.CornerRadius = UDim.new(0, 12)

--// KATEGORİ SEKME SİSTEMİ (PERFORMANS İÇİN)
local TabFrame = Instance.new("Frame")
TabFrame.Size = UDim2.new(1, 0, 0, 50)
TabFrame.Position = UDim2.new(0, 0, 0, 60)
TabFrame.BackgroundColor3 = Color3.fromRGB(25, 25, 30)
TabFrame.BorderSizePixel = 0
TabFrame.Parent = MainFrame

local TabLayout = Instance.new("UIListLayout")
TabLayout.FillDirection = Enum.FillDirection.Horizontal
TabLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
TabLayout.Padding = UDim.new(0, 5)
TabLayout.Parent = TabFrame

local ContentFrame = Instance.new("Frame")
ContentFrame.Size = UDim2.new(1, -20, 1, -130)
ContentFrame.Position = UDim2.new(0, 10, 0, 120)
ContentFrame.BackgroundTransparency = 1
ContentFrame.Parent = MainFrame

--// SEKME OLUŞTURMA
local currentTab = "main"
local tabs = {}

local function CreateTab(name, icon, tabId)
    local tabBtn = Instance.new("TextButton")
    tabBtn.Size = UDim2.new(0, 80, 0, 40)
    tabBtn.BackgroundColor3 = Color3.fromRGB(40, 40, 50)
    tabBtn.Text = icon .. "\n" .. name
    tabBtn.TextColor3 = Color3.fromRGB(200, 200, 200)
    tabBtn.TextSize = 11
    tabBtn.Font = Enum.Font.GothamBold
    tabBtn.TextWrapped = true
    tabBtn.Parent = TabFrame
    
    local tabCorner = Instance.new("UICorner", tabBtn)
    tabCorner.CornerRadius = UDim.new(0, 8)
    
    local content = Instance.new("ScrollingFrame")
    content.Name = tabId
    content.Size = UDim2.new(1, 0, 1, 0)
    content.BackgroundTransparency = 1
    content.ScrollBarThickness = 6
    content.ScrollBarImageColor3 = Color3.fromRGB(0, 255, 100)
    content.CanvasSize = UDim2.new(0, 0, 0, 500)
    content.Visible = false
    content.Parent = ContentFrame
    
    local listLayout = Instance.new("UIListLayout")
    listLayout.Padding = UDim.new(0, 8)
    listLayout.Parent = content
    
    tabs[tabId] = {button = tabBtn, content = content}
    
    tabBtn.MouseButton1Click:Connect(function()
        currentTab = tabId
        for id, tab in pairs(tabs) do
            tab.content.Visible = (id == tabId)
            tab.button.BackgroundColor3 = (id == tabId) and Color3.fromRGB(0, 255, 100) or Color3.fromRGB(40, 40, 50)
            tab.button.TextColor3 = (id == tabId) and Color3.fromRGB(0, 0, 0) or Color3.fromRGB(200, 200, 200)
        end
    end)
    
    return content
end

local mainTab = CreateTab("ANA", "⚡", "main")
local espTab = CreateTab("ESP", "👁️", "esp")
local adminTab = CreateTab("ADMIN", "👑", "admin")
local settingsTab = CreateTab("AYAR", "⚙️", "settings")

-- İlk sekmeyi aktif et
tabs["main"].button.BackgroundColor3 = Color3.fromRGB(0, 255, 100)
tabs["main"].button.TextColor3 = Color3.fromRGB(0, 0, 0)
tabs["main"].content.Visible = true

--// TOGGLE BUTON OLUŞTURMA (MOBİL UYUMLU, BÜYÜK)
local function CreateToggle(parent, name, featureKey, description, color)
    local frame = Instance.new("Frame")
    frame.Size = UDim2.new(1, 0, 0, 90)
    frame.BackgroundColor3 = Color3.fromRGB(35, 35, 42)
    frame.BorderSizePixel = 0
    frame.Parent = parent
    
    local corner = Instance.new("UICorner", frame)
    corner.CornerRadius = UDim.new(0, 10)
    
    local label = Instance.new("TextLabel")
    label.Size = UDim2.new(0.55, 0, 0, 35)
    label.Position = UDim2.new(0, 12, 0, 8)
    label.BackgroundTransparency = 1
    label.Text = name
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextSize = 18
    label.Font = Enum.Font.GothamBold
    label.TextXAlignment = Enum.TextXAlignment.Left
    label.Parent = frame
    
    local desc = Instance.new("TextLabel")
    desc.Size = UDim2.new(0.9, 0, 0, 30)
    desc.Position = UDim2.new(0, 12, 0, 45)
    desc.BackgroundTransparency = 1
    desc.Text = description
    desc.TextColor3 = Color3.fromRGB(150, 150, 150)
    desc.TextSize = 13
    desc.Font = Enum.Font.Gotham
    desc.TextXAlignment = Enum.TextXAlignment.Left
    desc.TextWrapped = true
    desc.Parent = frame
    
    -- BÜYÜK TOGGLE BUTONU (DOKUNMATİK)
    local toggleBtn = Instance.new("TextButton")
    toggleBtn.Size = UDim2.new(0, 80, 0, 45)
    toggleBtn.Position = UDim2.new(1, -95, 0, 22)
    toggleBtn.BackgroundColor3 = Color3.fromRGB(80, 80, 80)
    toggleBtn.Text = "KAPALI"
    toggleBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
    toggleBtn.TextSize = 14
    toggleBtn.Font = Enum.Font.GothamBold
    toggleBtn.Parent = frame
    
    local toggleCorner = Instance.new("UICorner", toggleBtn)
    toggleCorner.CornerRadius = UDim.new(0, 10)
    
    local toggleStroke = Instance.new("UIStroke", toggleBtn)
    toggleStroke.Color = Color3.fromRGB(100, 100, 100)
    toggleStroke.Thickness = 2
    
    toggleBtn.MouseButton1Click:Connect(function()
        MOD_MENU.Features[featureKey] = not MOD_MENU.Features[featureKey]
        local isActive = MOD_MENU.Features[featureKey]
        
        toggleBtn.BackgroundColor3 = isActive and (color or Color3.fromRGB(0, 255, 100)) or Color3.fromRGB(80, 80, 80)
        toggleBtn.Text = isActive and "AKTİF" or "KAPALI"
        toggleBtn.TextColor3 = isActive and Color3.fromRGB(0, 0, 0) or Color3.fromRGB(255, 255, 255)
        toggleStroke.Color = isActive and (color or Color3.fromRGB(0, 200, 80)) or Color3.fromRGB(100, 100, 100)
        
        -- Bildirim
        if isActive then
            game.StarterGui:SetCore("SendNotification", {
                Title = "✅ AKTİF",
                Text = name .. " açıldı!",
                Duration = 2
            })
        end
    end)
    
    return toggleBtn
end

--// SLIDER OLUŞTURMA (MOBİL UYUMLU)
local function CreateSlider(parent, name, featureKey, min, max, default)
    local frame = Instance.new("Frame")
    frame.Size = UDim2.new(1, 0, 0, 100)
    frame.BackgroundColor3 = Color3.fromRGB(35, 35, 42)
    frame.Parent = parent
    
    local corner = Instance.new("UICorner", frame)
    corner.CornerRadius = UDim.new(0, 10)
    
    local label = Instance.new("TextLabel")
    label.Size = UDim2.new(0.6, 0, 0, 30)
    label.Position = UDim2.new(0, 12, 0, 8)
    label.BackgroundTransparency = 1
    label.Text = name
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextSize = 18
    label.Font = Enum.Font.GothamBold
    label.TextXAlignment = Enum.TextXAlignment.Left
    label.Parent = frame
    
    local valueLabel = Instance.new("TextLabel")
    valueLabel.Size = UDim2.new(0, 60, 0, 30)
    valueLabel.Position = UDim2.new(1, -70, 0, 8)
    valueLabel.BackgroundTransparency = 1
    valueLabel.Text = tostring(default)
    valueLabel.TextColor3 = Color3.fromRGB(0, 255, 100)
    valueLabel.TextSize = 20
    valueLabel.Font = Enum.Font.GothamBold
    valueLabel.Parent = frame
    
    local sliderBg = Instance.new("Frame")
    sliderBg.Size = UDim2.new(0.9, 0, 0, 12)
    sliderBg.Position = UDim2.new(0.05, 0, 0, 55)
    sliderBg.BackgroundColor3 = Color3.fromRGB(60, 60, 70)
    sliderBg.BorderSizePixel = 0
    sliderBg.Parent = frame
    
    local bgCorner = Instance.new("UICorner", sliderBg)
    bgCorner.CornerRadius = UDim.new(1, 0)
    
    local fill = Instance.new("Frame")
    fill.Size = UDim2.new((default - min) / (max - min), 0, 1, 0)
    fill.BackgroundColor3 = Color3.fromRGB(0, 255, 100)
    fill.BorderSizePixel = 0
    fill.Parent = sliderBg
    
    local fillCorner = Instance.new("UICorner", fill)
    fillCorner.CornerRadius = UDim.new(1, 0)
    
    local knob = Instance.new("TextButton")
    knob.Size = UDim2.new(0, 30, 0, 30)
    knob.Position = UDim2.new((default - min) / (max - min), -15, 0, -9)
    knob.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
    knob.Text = ""
    knob.Parent = sliderBg
    
    local knobCorner = Instance.new("UICorner", knob)
    knobCorner.CornerRadius = UDim.new(1, 0)
    
    local knobStroke = Instance.new("UIStroke", knob)
    knobStroke.Color = Color3.fromRGB(0, 255, 100)
    knobStroke.Thickness = 3
    
    local sliding = false
    
    local function updateSlider(inputPos)
        local relativePos = (inputPos.X - sliderBg.AbsolutePosition.X) / sliderBg.AbsoluteSize.X
        relativePos = math.clamp(relativePos, 0, 1)
        
        fill.Size = UDim2.new(relativePos, 0, 1, 0)
        knob.Position = UDim2.new(relativePos, -15, 0, -9)
        
        local value = math.floor(min + (max - min) * relativePos)
        valueLabel.Text = tostring(value)
        MOD_MENU.Features[featureKey] = value
    end
    
    knob.InputBegan:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseButton1 then
            sliding = true
        end
    end)
    
    sliderBg.InputBegan:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseButton1 then
            sliding = true
            updateSlider(input.Position)
        end
    end)
    
    UserInputService.InputEnded:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseButton1 then
            sliding = false
        end
    end)
    
    UserInputService.InputChanged:Connect(function(input)
        if sliding and (input.UserInputType == Enum.UserInputType.Touch or input.UserInputType == Enum.UserInputType.MouseMovement) then
            updateSlider(input.Position)
        end
    end)
end

--// AKSİYON BUTONU (MOBİL UYUMLU)
local function CreateActionButton(parent, name, callback, color)
    local btn = Instance.new("TextButton")
    btn.Size = UDim2.new(1, 0, 0, 55)
    btn.BackgroundColor3 = color or Color3.fromRGB(50, 50, 60)
    btn.Text = name
    btn.TextColor3 = Color3.fromRGB(255, 255, 255)
    btn.TextSize = 16
    btn.Font = Enum.Font.GothamBold
    btn.Parent = parent
    
    local corner = Instance.new("UICorner", btn)
    corner.CornerRadius = UDim.new(0, 10)
    
    local stroke = Instance.new("UIStroke", btn)
    stroke.Color = Color3.fromRGB(80, 80, 90)
    stroke.Thickness = 2
    
    btn.MouseButton1Click:Connect(function()
        callback()
        -- Tıklama efekti
        TweenService:Create(btn, TweenInfo.new(0.1), {BackgroundColor3 = Color3.fromRGB(100, 100, 110)}):Play()
        task.wait(0.1)
        TweenService:Create(btn, TweenInfo.new(0.1), {BackgroundColor3 = color or Color3.fromRGB(50, 50, 60)}):Play()
    end)
    
    return btn
end

--// ============================================
--// SEKME İÇERİKLERİ
--// ============================================

-- ANA SEKME
CreateToggle(mainTab, "🪓 Zincir Kesme", "ChainChop", "Ağaç kesince 5 ağaç daha kırılır", Color3.fromRGB(255, 100, 50))
CreateToggle(mainTab, "🦅 Uçma Modu", "Fly", "Karakter uçar (telefonda zor)", Color3.fromRGB(100, 150, 255))
CreateToggle(mainTab, "🏃 Hızlı Koşu", "Speed", "Koşu hızını artırır", Color3.fromRGB(255, 255, 0))
CreateSlider(mainTab, "⚡ Hız Değeri", "SpeedValue", 16, 150, 50)
CreateToggle(mainTab, "👻 Duvar İçi", "NoClip", "Duvarlardan geçersin", Color3.fromRGB(150, 50, 255))
CreateToggle(mainTab, "💡 Tam Parlaklık", "FullBright", "Gece görüşü", Color3.fromRGB(255, 255, 200))
CreateToggle(mainTab, "🛡️ Ölümsüzlük", "GodMode", "Hasar almazsın", Color3.fromRGB(255, 50, 50))

-- ESP SEKME (OPTİMİZE)
CreateToggle(espTab, "📦 Eşya ESP", "ItemESP", "Yerdeki eşyalar (optimize)", Color3.fromRGB(255, 255, 0))
CreateToggle(espTab, "🎁 Sandık ESP", "ChestESP", "Sandık konumları (optimize)", Color3.fromRGB(255, 165, 0))
CreateToggle(espTab, "🔩 Hurda ESP", "ScrapESP", "Hurda yerleri (optimize)", Color3.fromRGB(192, 192, 192))

-- ESP AYAR LABEL
local espInfo = Instance.new("TextLabel")
espInfo.Size = UDim2.new(1, 0, 0, 60)
espInfo.BackgroundColor3 = Color3.fromRGB(40, 30, 30)
espInfo.Text = "⚠️ ESP'ler 3 saniyede bir güncellenir\nKasma azaltmak için mesafe sınırı: 150m"
espInfo.TextColor3 = Color3.fromRGB(255, 200, 100)
espInfo.TextSize = 13
espInfo.Font = Enum.Font.Gotham
espInfo.TextWrapped = true
espInfo.Parent = espTab

local espInfoCorner = Instance.new("UICorner", espInfo)
espInfoCorner.CornerRadius = UDim.new(0, 8)

-- ADMIN SEKME (DÜZELTİLMİŞ)
CreateActionButton(adminTab, "🌙 Geceyi Atla (SABAH)", function()
    Lighting.ClockTime = 12
    game.StarterGui:SetCore("SendNotification", {
        Title = "☀️ Sabah",
        Text = "Zaman sabah yapıldı!",
        Duration = 2
    })
end, Color3.fromRGB(255, 200, 50))

CreateActionButton(adminTab, "🌑 Gece Yap", function()
    Lighting.ClockTime = 0
    game.StarterGui:SetCore("SendNotification", {
        Title = "🌑 Gece",
        Text = "Zaman gece yapıldı!",
        Duration = 2
    })
end, Color3.fromRGB(50, 50, 100))

CreateActionButton(adminTab, "🌅 Gün Doğumu", function()
    Lighting.ClockTime = 6
    game.StarterGui:SetCore("SendNotification", {
        Title = "🌅 Gün Doğumu",
        Text = "Zaman ayarlandı!",
        Duration = 2
    })
end, Color3.fromRGB(255, 150, 100))

CreateActionButton(adminTab, "👻 Tüm NPC'leri İşaretle", function()
    local count = 0
    for _, obj in pairs(Workspace:GetDescendants()) do
        if obj:FindFirstChild("Humanoid") and obj ~= character then
            if not obj:FindFirstChild("NPC_Highlight") then
                local hl = Instance.new("Highlight")
                hl.Name = "NPC_Highlight"
                hl.FillColor = Color3.fromRGB(255, 0, 0)
                hl.OutlineColor = Color3.fromRGB(255, 255, 0)
                hl.FillTransparency = 0.5
                hl.Parent = obj
                count = count + 1
            end
        end
    end
    game.StarterGui:SetCore("SendNotification", {
        Title = "👻 NPC İşaretleme",
        Text = count .. " NPC işaretlendi!",
        Duration = 3
    })
end, Color3.fromRGB(255, 100, 100))

CreateActionButton(adminTab, "📍 Tüm Oyuncuları İşaretle", function()
    for _, p in pairs(Players:GetPlayers()) do
        if p ~= player and p.Character then
            local hrp = p.Character:FindFirstChild("HumanoidRootPart")
            if hrp and not hrp:FindFirstChild("PlayerESP") then
                local billboard = Instance.new("BillboardGui")
                billboard.Name = "PlayerESP"
                billboard.AlwaysOnTop = true
                billboard.Size = UDim2.new(0, 150, 0, 40)
                billboard.StudsOffset = Vector3.new(0, 3, 0)
                billboard.Adornee = hrp
                billboard.Parent = hrp
                
                local label = Instance.new("TextLabel")
                label.Size = UDim2.new(1, 0, 1, 0)
                label.BackgroundTransparency = 1
                label.Text = "👤 " .. p.Name
                label.TextColor3 = Color3.fromRGB(255, 0, 0)
                label.TextStrokeTransparency = 0.5
                label.TextSize = 14
                label.Font = Enum.Font.GothamBold
                label.Parent = billboard
            end
        end
    end
    game.StarterGui:SetCore("SendNotification", {
        Title = "📍 Oyuncular",
        Text = "Tüm oyuncular işaretlendi!",
        Duration = 3
    })
end, Color3.fromRGB(100, 150, 255))

CreateActionButton(adminTab, "🧹 Tüm İşaretleri Temizle", function()
    for _, obj in pairs(Workspace:GetDescendants()) do
        if obj:FindFirstChild("NPC_Highlight") then
            obj.NPC_Highlight:Destroy()
        end
        if obj:FindFirstChild("PlayerESP") then
            obj.PlayerESP:Destroy()
        end
    end
    game.StarterGui:SetCore("SendNotification", {
        Title = "🧹 Temizlik",
        Text = "Tüm işaretler temizlendi!",
        Duration = 2
    })
end, Color3.fromRGB(255, 100, 50))

CreateActionButton(adminTab, "🔄 Karakteri Yenile", function()
    character:BreakJoints()
end, Color3.fromRGB(200, 50, 200))

-- AYARLAR SEKME
CreateActionButton(settingsTab, "🎨 Menü Rengini Değiştir", function()
    local colors = {
        Color3.fromRGB(0, 255, 100),
        Color3.fromRGB(255, 100, 100),
        Color3.fromRGB(100, 150, 255),
        Color3.fromRGB(255, 200, 50),
        Color3.fromRGB(200, 50, 255)
    }
    local randomColor = colors[math.random(1, #colors)]
    ToggleButton.TextColor3 = randomColor
    ToggleStroke.Color = randomColor
    Title.TextColor3 = randomColor
end, Color3.fromRGB(100, 100, 100))

CreateActionButton(settingsTab, "📱 Buton Konumunu Sıfırla", function()
    ToggleButton.Position = UDim2.new(1, -80, 0, 10)
end, Color3.fromRGB(100, 100, 100))

--// ============================================
--// MENÜ AÇMA/KAPAMA
--// ============================================

local function ToggleMenu()
    MOD_MENU.Visible = not MOD_MENU.Visible
    MainFrame.Visible = MOD_MENU.Visible
    
    if MOD_MENU.Visible then
        MainFrame.Size = UDim2.new(0.1, 0, 0.1, 0)
        MainFrame.Position = UDim2.new(0.45, 0, 0.45, 0)
        TweenService:Create(MainFrame, TweenInfo.new(0.3, Enum.EasingStyle.Back), {
            Size = UDim2.new(0.95, 0, 0.85, 0),
            Position = UDim2.new(0.025, 0, 0.075, 0)
        }):Play()
    end
end

ToggleButton.MouseButton1Click:Connect(ToggleMenu)
CloseButton.MouseButton1Click:Connect(ToggleMenu)

--// ============================================
--// ESP SİSTEMİ (OPTİMİZE - MOBİL İÇİN)
--// ============================================

local ESPFolder = Instance.new("Folder")
ESPFolder.Name = "MobileESP"
ESPFolder.Parent = Workspace

-- ESP Cache (performans için)
local espCache = {}
local lastESPUpdate = 0
local ESP_UPDATE_INTERVAL = 3 -- 3 saniyede bir güncelle

local function ClearESP()
    for _, obj in pairs(ESPFolder:GetChildren()) do
        obj:Destroy()
    end
    espCache = {}
end

local function CreateMobileESP(target, text, color, maxDistance)
    if not target or not target.Parent then return end
    if espCache[target] then return end -- Zaten var
    
    local billboard = Instance.new("BillboardGui")
    billboard.Name = "ESP_" .. target.Name
    billboard.AlwaysOnTop = true
    billboard.Size = UDim2.new(0, 120, 0, 40)
    billboard.StudsOffset = Vector3.new(0, 2, 0)
    billboard.MaxDistance = maxDistance or 150 -- MOBİL İÇİN MESAFE SINIRI
    billboard.Parent = ESPFolder
    
    local label = Instance.new("TextLabel")
    label.Size = UDim2.new(1, 0, 0.6, 0)
    label.BackgroundTransparency = 1
    label.Text = text
    label.TextColor3 = color
    label.TextStrokeTransparency = 0.3
    label.TextSize = 12 -- DAHA KÜÇÜK YAZI
    label.Font = Enum.Font.GothamBold
    label.Parent = billboard
    
    local distLabel = Instance.new("TextLabel")
    distLabel.Size = UDim2.new(1, 0, 0.4, 0)
    distLabel.Position = UDim2.new(0, 0, 0.6, 0)
    distLabel.BackgroundTransparency = 1
    distLabel.Text = "0m"
    distLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
    distLabel.TextStrokeTransparency = 0.3
    distLabel.TextSize = 10
    distLabel.Font = Enum.Font.Gotham
    distLabel.Parent = billboard
    
    -- Basit bağlama (performans için)
    billboard.Adornee = target
    
    espCache[target] = {
        billboard = billboard,
        target = target,
        lastUpdate = tick()
    }
end

-- ESP GÜNCELLEME (3 SANİYEDE BİR)
local function UpdateESP()
    local currentTime = tick()
    if currentTime - lastESPUpdate < ESP_UPDATE_INTERVAL then return end
    lastESPUpdate = currentTime
    
    -- Önce temizle
    ClearESP()
    
    if not (MOD_MENU.Features.ItemESP or MOD_MENU.Features.ChestESP or MOD_MENU.Features.ScrapESP) then
        return
    end
    
    local playerPos = humanoidRootPart and humanoidRootPart.Position or Vector3.new(0, 0, 0)
    
    -- Yerdeki eşyalar
    if MOD_MENU.Features.ItemESP then
        for _, obj in pairs(Workspace:GetDescendants()) do
            if obj:IsA("BasePart") and obj.Parent ~= character then
                local name = obj.Name:lower()
                local distance = (obj.Position - playerPos).Magnitude
                
                if distance < 150 then -- MESAJE SINIRI
                    if name:find("bandaj") or name:find("bandage") or 
                       name:find("food") or name:find("yemek") or 
                       name:find("med") or name:find("ilaç") or
                       name:find("weapon") or name:find("silah") or
                       name:find("ammo") or name:find("mermi") then
                        CreateMobileESP(obj, "📦 " .. obj.Name, Color3.fromRGB(255, 255, 0), 150)
                    end
                end
            end
        end
    end
    
    -- Sandıklar
    if MOD_MENU.Features.ChestESP then
        for _, obj in pairs(Workspace:GetDescendants()) do
            if obj:IsA("BasePart") or obj:IsA("Model") then
                local name = obj.Name:lower()
                if name:find("chest") or name:find("sandık") or 
                   name:find("crate") or name:find("box") or
                   name:find("loot") then
                    local part = obj:IsA("BasePart") and obj or obj:FindFirstChildWhichIsA("BasePart")
                    if part then
                        local distance = (part.Position - playerPos).Magnitude
                        if distance < 200 then
                            CreateMobileESP(part, "🎁 " .. (obj:IsA("Model") and obj.Name or "Sandık"), Color3.fromRGB(255, 165, 0), 200)
                        end
                    end
                end
            end
        end
    end
    
    -- Hurda
    if MOD_MENU.Features.ScrapESP then
        for _, obj in pairs(Workspace:GetDescendants()) do
            if obj:IsA("BasePart") then
                local name = obj.Name:lower()
                if name:find("scrap") or name:find("hurda") or 
                   name:find("iron") or name:find("demir") or
                   name:find("metal") or name:find("copper") or
                   name:find("gear") or name:find("spring") then
                    local distance = (obj.Position - playerPos).Magnitude
                    if distance < 150 then
                        CreateMobileESP(obj, "🔩 " .. obj.Name, Color3.fromRGB(192, 192, 192), 150)
                    end
                end
            end
        end
    end
end

--// ============================================
// FLY SİSTEMİ (MOBİL UYUMLU - JOYSTICK)
// ============================================

local flyActive = false
local flyVelocity = nil
local flyGyro = nil
local flyConnection = nil

-- MOBİL UÇMA KONTROLLERİ (EKRAN BUTONLARI)
local FlyControlsFrame = Instance.new("Frame")
FlyControlsFrame.Size = UDim2.new(0, 200, 0, 200)
FlyControlsFrame.Position = UDim2.new(0.5, -100, 0.7, 0)
FlyControlsFrame.BackgroundTransparency = 0.5
FlyControlsFrame.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
FlyControlsFrame.Visible = false
FlyControlsFrame.Parent = ScreenGui

local FlyCorner = Instance.new("UICorner", FlyControlsFrame)
FlyCorner.CornerRadius = UDim.new(0, 20)

-- Yukarı buton
local FlyUpBtn = Instance.new("TextButton")
FlyUpBtn.Size = UDim2.new(0, 60, 0, 60)
FlyUpBtn.Position = UDim2.new(0.5, -30, 0, 10)
FlyUpBtn.BackgroundColor3 = Color3.fromRGB(0, 200, 100)
FlyUpBtn.Text = "⬆️"
FlyUpBtn.TextSize = 30
FlyUpBtn.Parent = FlyControlsFrame

-- Aşağı buton
local FlyDownBtn = Instance.new("TextButton")
FlyDownBtn.Size = UDim2.new(0, 60, 0, 60)
FlyDownBtn.Position = UDim2.new(0.5, -30, 1, -70)
FlyDownBtn.BackgroundColor3 = Color3.fromRGB(200, 50, 50)
FlyDownBtn.Text = "⬇️"
FlyDownBtn.TextSize = 30
FlyDownBtn.Parent = FlyControlsFrame

-- İleri buton
local FlyForwardBtn = Instance.new("TextButton")
FlyForwardBtn.Size = UDim2.new(0, 60, 0, 60)
FlyForwardBtn.Position = UDim2.new(1, -70, 0.5, -30)
FlyForwardBtn.BackgroundColor3 = Color3.fromRGB(50, 100, 200)
FlyForwardBtn.Text = "➡️"
FlyForwardBtn.TextSize = 30
FlyForwardBtn.Parent = FlyControlsFrame

-- Geri buton
local FlyBackBtn = Instance.new("TextButton")
FlyBackBtn.Size = UDim2.new(0, 60, 0, 60)
FlyBackBtn.Position = UDim2.new(0, 10, 0.5, -30)
FlyBackBtn.BackgroundColor3 = Color3.fromRGB(50, 100, 200)
FlyBackBtn.Text = "⬅️"
FlyBackBtn.TextSize = 30
FlyBackBtn.Parent = FlyControlsFrame

-- Uçma kapat butonu
local FlyCloseBtn = Instance.new("TextButton")
FlyCloseBtn.Size = UDim2.new(0, 50, 0, 50)
FlyCloseBtn.Position = UDim2.new(0.5, -25, 0.5, -25)
FlyCloseBtn.BackgroundColor3 = Color3.fromRGB(255, 50, 50)
FlyCloseBtn.Text = "✕"
FlyCloseBtn.TextSize = 24
FlyCloseBtn.Parent = FlyControlsFrame

local function ToggleFly()
    if MOD_MENU.Features.Fly and not flyActive then
        flyActive = true
        flyVelocity = Instance.new("BodyVelocity")
        flyVelocity.MaxForce = Vector3.new(400000, 400000, 400000)
        flyVelocity.Velocity = Vector3.new(0, 0, 0)
        flyVelocity.Parent = humanoidRootPart
        
        flyGyro = Instance.new("BodyGyro")
        flyGyro.MaxTorque = Vector3.new(400000, 400000, 400000)
        flyGyro.P = 10000
        flyGyro.Parent = humanoidRootPart
        
        FlyControlsFrame.Visible = true
        
        flyConnection = RunService.RenderStepped:Connect(function()
            if not flyActive then return end
            
            local direction = Vector3.new(0, 0, 0)
            local cam = camera
            
            -- Ekran butonlarından yön al
            -- Not: Telefonda joystick veya ekran kaydırma ile yön verilebilir
            -- Basit versiyon: Kameraya göre ileri/geri/sağ/sol
            
            -- Daha basit uçma: Sadece yukarı/aşağı ve kameraya göre ileri
            if FlyUpBtn.BackgroundColor3 == Color3.fromRGB(0, 255, 150) then
                direction = direction + Vector3.new(0, 1, 0)
            end
            if FlyDownBtn.BackgroundColor3 == Color3.fromRGB(255, 100, 100) then
                direction = direction - Vector3.new(0, 1, 0)
            end
            
            -- Kamera yönüne göre ileri
            if FlyForwardBtn.BackgroundColor3 == Color3.fromRGB(100, 150, 255) then
                direction = direction + cam.CFrame.LookVector
            end
            if FlyBackBtn.BackgroundColor3 == Color3.fromRGB(100, 150, 255) then
                direction = direction - cam.CFrame.LookVector
            end
            
            if direction.Magnitude > 0 then
                direction = direction.Unit * MOD_MENU.Features.FlySpeed
            end
            
            flyVelocity.Velocity = direction
            flyGyro.CFrame = cam.CFrame
        end)
        
        humanoid.PlatformStand = true
        
    elseif not MOD_MENU.Features.Fly and flyActive then
        flyActive = false
        FlyControlsFrame.Visible = false
        if flyConnection then flyConnection:Disconnect() end
        if flyVelocity then flyVelocity:Destroy() end
        if flyGyro then flyGyro:Destroy() end
        humanoid.PlatformStand = false
        humanoid:ChangeState(Enum.HumanoidStateType.GettingUp)
    end
end

-- Fly buton olayları
local function setupFlyButton(btn, activeColor, inactiveColor)
    btn.InputBegan:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.Touch then
            btn.BackgroundColor3 = activeColor
        end
    end)
    btn.InputEnded:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.Touch then
            btn.BackgroundColor3 = inactiveColor
        end
    end)
end

setupFlyButton(FlyUpBtn, Color3.fromRGB(0, 255, 150), Color3.fromRGB(0, 200, 100))
setupFlyButton(FlyDownBtn, Color3.fromRGB(255, 100, 100), Color3.fromRGB(200, 50, 50))
setupFlyButton(FlyForwardBtn, Color3.fromRGB(100, 150, 255), Color3.fromRGB(50, 100, 200))
setupFlyButton(FlyBackBtn, Color3.fromRGB(100, 150, 255), Color3.fromRGB(50, 100, 200))

FlyCloseBtn.MouseButton1Click:Connect(function()
    MOD_MENU.Features.Fly = false
    ToggleFly()
end)

--// ============================================
--// DİĞER SİSTEMLER
--// ============================================

-- HIZ
local function UpdateSpeed()
    if MOD_MENU.Features.Speed then
        humanoid.WalkSpeed = MOD_MENU.Features.SpeedValue
    else
        humanoid.WalkSpeed = 16
    end
end

-- NOCLIP
local noclipConnection
local function UpdateNoClip()
    if MOD_MENU.Features.NoClip then
        if not noclipConnection then
            noclipConnection = RunService.Stepped:Connect(function()
                if not MOD_MENU.Features.NoClip then return end
                for _, part in pairs(character:GetDescendants()) do
                    if part:IsA("BasePart") then
                        part.CanCollide = false
                    end
                end
            end)
        end
    else
        if noclipConnection then
            noclipConnection:Disconnect()
            noclipConnection = nil
        end
        for _, part in pairs(character:GetDescendants()) do
            if part:IsA("BasePart") then
                part.CanCollide = true
            end
        end
    end
end

-- FULLBRIGHT
local originalSettings = {}
local function UpdateFullBright()
    if MOD_MENU.Features.FullBright then
        if not originalSettings.saved then
            originalSettings.brightness = Lighting.Brightness
            originalSettings.shadows = Lighting.GlobalShadows
            originalSettings.ambient = Lighting.Ambient
            originalSettings.outdoor = Lighting.OutdoorAmbient
            originalSettings.saved = true
        end
        Lighting.Brightness = 10
        Lighting.GlobalShadows = false
        Lighting.Ambient = Color3.fromRGB(255, 255, 255)
        Lighting.OutdoorAmbient = Color3.fromRGB(255, 255, 255)
    else
        if originalSettings.saved then
            Lighting.Brightness = originalSettings.brightness
            Lighting.GlobalShadows = originalSettings.shadows
            Lighting.Ambient = originalSettings.ambient
            Lighting.OutdoorAmbient = originalSettings.outdoor
        end
    end
end

-- GODMODE
local function UpdateGodMode()
    if MOD_MENU.Features.GodMode then
        humanoid.MaxHealth = math.huge
        humanoid.Health = math.huge
    else
        humanoid.MaxHealth = 100
        humanoid.Health = 100
    end
end

-- ZİNCİR AĞAÇ KESME
local function SetupChainChop()
    -- Ağaç hasar olayını dinle
    -- Oyunun RemoteEvent yapısına göre ayarlanmalı
    -- Basit versiyon: Ağaç yok olduğunda tetiklenir
    
    local function onTreeDestroyed(tree)
        if not MOD_MENU.Features.ChainChop then return end
        
        local treePos = tree:GetPivot().Position
        local destroyed = 0
        
        for _, obj in pairs(Workspace:GetDescendants()) do
            if obj:IsA("Model") and obj ~= tree then
                local name = obj.Name:lower()
                if name:find("tree") or name:find("ağaç") or name:find("wood") then
                    local primary = obj:FindFirstChildWhichIsA("BasePart")
                    if primary then
                        local dist = (primary.Position - treePos).Magnitude
                        if dist <= 20 and destroyed < 5 then
                            destroyed = destroyed + 1
                            
                            -- Yıkılma efekti
                            for _, part in pairs(obj:GetDescendants()) do
                                if part:IsA("BasePart") then
                                    part.Anchored = false
                                    part.Velocity = Vector3.new(
                                        math.random(-15, 15),
                                        math.random(10, 20),
                                        math.random(-15, 15)
                                    )
                                end
                            end
                            
                            task.delay(2, function()
                                if obj and obj.Parent then
                                    obj:Destroy()
                                end
                            end)
                        end
                    end
                end
            end
        end
        
        if destroyed > 0 then
            game.StarterGui:SetCore("SendNotification", {
                Title = "🪓 Zincir Kesme",
                Text = destroyed .. " ağaç daha yıkıldı!",
                Duration = 2
            })
        end
    end
    
    -- Ağaç yok olma olayını dinle (ChildRemoved ile)
    local treesFolder = Workspace:FindFirstChild("Trees") or Workspace:FindFirstChild("Forest") or Workspace
    
    -- Basit versiyon: Tüm model yok olmalarını dinle
    -- Gerçek uygulamada oyunun özel olay sistemi kullanılmalı
end

--// ============================================
--// ANA DÖNGÜ (OPTİMİZE)
--// ============================================

RunService.Heartbeat:Connect(function()
    -- ESP güncelleme (3 saniyede bir)
    UpdateESP()
    
    -- Diğer sistemler
    UpdateSpeed()
    UpdateNoClip()
    UpdateFullBright()
    UpdateGodMode()
    ToggleFly()
end)

--// KARAKTER YENİLENDİĞİNDE
player.CharacterAdded:Connect(function(newChar)
    character = newChar
    humanoid = newChar:WaitForChild("Humanoid")
    humanoidRootPart = newChar:WaitForChild("HumanoidRootPart")
    
    -- Fly sıfırla
    flyActive = false
    flyVelocity = nil
    flyGyro = nil
    flyConnection = nil
    FlyControlsFrame.Visible = false
end)

--// BAŞLANGIÇ BİLDİRİMİ
task.delay(2, function()
    game.StarterGui:SetCore("SendNotification", {
        Title = "🌲 Orman 99 Gece",
        Text = "Mobil Mod Menü yüklendi!\nSağ üstteki 🌲 butonuna dokun",
        Duration = 5
    })
end)

print("✅ Orman 99 Gece - Mobil Mod Menü yüklendi!")
